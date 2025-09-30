import re
import unicodedata
from typing import List, Tuple, Dict, Any
from utils.Logger import get_logger

logger = get_logger()

# Character map for fuzzy matching
char_map = {
    'a': '[aAáàâäãåā@4]', 'b': '[bB8]', 'c': '[cCçćč]', 'd': '[dDđ]', 'e': '[eEéèêëē3]',
    'f': '[fF]', 'g': '[gGğ9]', 'h': '[hH]', 'i': '[iIíìîïİ1!|]', 'j': '[jJ]',
    'k': '[kKqQ]', 'l': '[lL1|]', 'm': '[mM]', 'n': '[nNñń]', 'o': '[oOóòôöõ0]',
    'p': '[pP]', 'q': '[qQ]', 'r': '[rR]', 's': '[sSşš5$]', 't': '[tT7+]',
    'u': '[uUüùûú]', 'v': '[vV]', 'w': '[wW]', 'x': '[xX×]', 'y': '[yYÿ]',
    'z': '[zZž2]', '0': '[0oO]', '1': '[1iI!|lL]', '2': '[2zZ]', '3': '[3eE]',
    '4': '[4aA]', '5': '[5sS$]', '6': '[6gG]', '7': '[7tT+]', '8': '[8bB]',
    '9': '[9gG]', '.': '[\\.·]', ',': '[,]', '?': '[\\?¿]', '!': '[!1|I]',
    '@': '[@aA]', '#': '[#]', '$': '[$sS5]', '%': '[%]', '&': '[&]', '*': '[*]',
    '(': '[\\(\\[]', ')': '[\\)\\]]', '-': '[-–—]', '_': '[_]', '=': '[=]',
    '+': '[+]', ':': '[:]', ';': '[;]', '"': '["“”]', "'": "['‘’]", '/': '[/]',
    '\\': '[\\\\]', '<': '[<]', '>': '[>]', '^': '[^]', '`': '[`]', '~': '[~]',
    '|': '[|I1!]', ' ': '\\s'
}

# Predefined patterns from validation.py
PREDEFINED_PATTERNS = {
    'email': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$',
    'iranian_phone': r'^(?:00989|\+989|09)[0-9]{9}$',
    'international_phone': r'^\+?[1-9]\d{1,14}$',
    'url': r'^(?:https?://)?(?:www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?$',
    'date_iso': r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',
    'date_eu': r'^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$',
    'time': r'^(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?$',
    'uuid4': r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89ABab][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$',
    'iran_national_code': r'^[0-9]{10}$',
    'isbn10': r'^(?:\d{9}X|\d{10})$',
    'isbn13': r'^[0-9]{13}$',
    'hex_color': r'^#(?:[0-9A-Fa-f]{3}){1,2}$',
    'scientific_number': r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)$',
    'thousand_sep_number': r'^[0-9]{1,3}(?:,[0-9]{3})*(?:\.\d+)?$',
    'mention': r'^@[A-Za-z0-9_]+$',
    'markdown_link': r'^\[.+?\]\([^)]+\)$',
    'html_tag': r'^<[^>]+>$',
    'multiple_emails': r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:\s*,\s*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})*$',
    'base64': r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
}


def _char_type(ch: str) -> str:
    """Return a short type name for the character using Unicode category."""
    if ch.isdigit():
        return "DIGIT"
    if ch.isspace():
        return "SPACE"
    cat = unicodedata.category(ch)
    if cat[0] == "L":
        return "LETTER"
    if cat[0] == "N":
        return "NUMBER"
    if cat[0] == "P":
        return "PUNCT"
    if cat[0] == "S":
        return "SYMBOL"
    if cat[0] == "Z":
        return "SPACE"
    return "OTHER"


def _repr_for_char(ch: str, use_char_map: bool = True) -> Tuple[str, str]:
    """
    Returns (repr_token, desc) for a single character.
    repr_token: Regex fragment (no quantifier).
    desc: Human-friendly name.
    """
    t = _char_type(ch)
    if use_char_map and ch in char_map:
        return char_map[ch], f"fuzzy '{ch}'"
    if t == "DIGIT":
        return r"\d", "digit"
    if t == "LETTER":
        return r"[^\W\d_]", "letter"
    if t == "SPACE":
        return r"\s", "whitespace"
    if t == "PUNCT":
        return re.escape(ch), f"punctuation '{ch}'"
    if t == "SYMBOL":
        return re.escape(ch), f"symbol '{ch}'"
    return re.escape(ch), f"literal '{ch}'"


def _build_fragments_and_groups(text: str, use_char_map: bool) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Shared logic to tokenize and group characters.
    Returns (fragments, groups) where fragments are per-char and groups are compressed.
    """
    if not isinstance(text, str):
        logger.error(f"Input must be a string, got {type(text)}")
        raise TypeError("Input must be a string")
    if not text:
        logger.warning("Empty input provided")
        return [], []

    # Build per-character fragments
    fragments = []
    for ch in text:
        frag, desc = _repr_for_char(ch, use_char_map)
        frag_type = _char_type(ch)
        fragments.append({"char": ch, "type": frag_type, "pattern": frag, "desc": desc})

    # Compress into groups
    groups = []
    i = 0
    n = len(fragments)
    while i < n:
        cur = fragments[i]
        j = i + 1
        if cur["type"] in ("PUNCT", "SYMBOL"):
            chars = [cur["char"]]
            patterns = [cur["pattern"]]
            while j < len(fragments) and fragments[j]["pattern"] == cur["pattern"]:
                chars.append(fragments[j]["char"])
                patterns.append(fragments[j]["pattern"])
                j += 1
            if len(set(chars)) == 1:
                pat = patterns[0]
                cnt = len(chars)
                groups.append({
                    "type": cur["type"],
                    "name": cur["desc"],
                    "pattern": pat,
                    "count": cnt,
                    "example_chars": list(set(chars))
                })
            else:
                unique = []
                for p, c in zip(patterns, chars):
                    if p not in unique:
                        unique.append(p)
                class_body = "".join(unique)
                class_pattern = f"[{class_body}]"
                cnt = len(chars)
                groups.append({
                    "type": "PUNCT_OR_SYMBOL",
                    "name": "punctuation_or_symbol",
                    "pattern": class_pattern,
                    "count": cnt,
                    "example_chars": list(dict.fromkeys(chars))
                })
            i = j
        else:
            pat = cur["pattern"]
            cnt = 1
            while j < n and fragments[j]["pattern"] == pat and fragments[j]["type"] == cur["type"]:
                cnt += 1
                j += 1
            groups.append({
                "type": cur["type"],
                "name": cur["desc"],
                "pattern": pat,
                "count": cnt,
                "example_chars": [cur["char"]]
            })
            i = j

    logger.debug(f"Generated {len(groups)} groups for input: {text}")
    return fragments, groups


def string_to_regex(text: str, *, use_anchors: bool = False, use_char_map: bool = True, detailed: bool = False) -> str | \
                                                                                                                   Tuple[
                                                                                                                       str,
                                                                                                                       Dict[
                                                                                                                           str, Any]]:
    """
    Convert an input string into a regex pattern.
    If use_anchors=True, wraps with ^...$; if use_char_map=True, uses char_map for fuzzy matching.
    If detailed=True, returns (pattern, details) with validation info.

    Returns:
        str: Regex pattern if detailed=False.
        Tuple[str, Dict[str, Any]]: (pattern, details) if detailed=True, where details include:
            - valid: bool (pattern matches input)
            - score: float (generalization score based on variants)
            - sample_matches: List[str] (example strings that match)
            - explanation: str (human-readable validation summary)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    try:
        logger.info(f"Generating regex for: {text}")
        _, groups = _build_fragments_and_groups(text, use_char_map)
        regex_parts = []
        for g in groups:
            pat = g["pattern"]
            cnt = g["count"]
            if cnt == 1:
                regex_fragment = pat
            elif pat == r"\d":
                regex_fragment = rf"\d{{{cnt}}}"
            elif pat.startswith("[") and pat.endswith("]"):
                regex_fragment = rf"{pat}{{{cnt}}}"
            else:
                regex_fragment = f"(?:{pat}){{{cnt}}}"

            regex_parts.append(regex_fragment)

        pattern = "".join(regex_parts)
        pattern = f"^{pattern}$" if use_anchors else f"\\b{pattern}\\b"

        if not detailed:
            logger.info(f"Generated pattern: {pattern}")
            return pattern

        # Apply anchors or word boundaries carefully
        if use_anchors:
            # avoid double anchors
            if not pattern.startswith("^"):
                pattern = f"^{pattern}"
            if not pattern.endswith("$"):
                pattern = f"{pattern}$"
        elif any(ch.isalnum() for ch in text):
            # avoid double \b
            if not (pattern.startswith(r"\b") and pattern.endswith(r"\b")):
                pattern = f"\\b{pattern}\\b"

        elif any(ch.isalnum() for ch in text):
            # avoid double \b
            if not (pattern.startswith(r"\b") and pattern.endswith(r"\b")):
                pattern = f"\\b{pattern}\\b"

        # Detailed output: validate and score
        details = {"valid": False, "score": 0.0, "sample_matches": [], "explanation": ""}
        try:
            compiled = re.compile(pattern)
            details["valid"] = compiled.fullmatch(text) is not None
            # Generate simple variants (e.g., shift letters/digits)
            variants = [text]
            for _ in range(3):
                var = list(text)
                for i in range(len(var)):
                    if var[i].isalpha() and var[i].lower() in char_map:
                        # Use a char from the char_map class
                        opts = re.findall(r'[a-zA-Z]', char_map.get(var[i].lower(), var[i]))
                        var[i] = opts[0] if opts else var[i]
                    elif var[i].isdigit():
                        var[i] = str((int(var[i]) + 1) % 10)
                variants.append(''.join(var))
            matches = [v for v in variants if compiled.fullmatch(v)]
            details["score"] = len(matches) / len(variants)
            details["sample_matches"] = matches[:3]
            details["explanation"] = (
                f"Pattern matches original: {details['valid']}. "
                f"Generalizes to {details['score'] * 100:.0f}% of {len(variants)} variants. "
                f"Sample matches: {', '.join(details['sample_matches'][:3]) or 'none'}"
            )
            logger.debug(f"Validation details: {details['explanation']}")
        except re.error as e:
            logger.error(f"Invalid regex pattern: {e}")
            details["explanation"] = f"Invalid regex: {e}"
        # pattern = unicodedata.name(pattern)
        return pattern, details

    except Exception as e:
        logger.error(f"Error building pattern: {e}")
        if detailed:
            return f"(Error: {e})", {"valid": False, "score": 0.0, "sample_matches": [], "explanation": f"Error: {e}"}
        return f"(Error: {e})"


def string_to_breakdown(text: str, *, use_char_map: bool = True, detailed: bool = False) -> List[Dict[str, Any]]:
    """
    Convert an input string into a structured breakdown of its regex components.
    If detailed=True, includes Unicode category and variant matches for each group.

    Returns:
        List[Dict[str, Any]]: Breakdown list with fields:
            - type: DIGIT, LETTER, SPACE, PUNCT, SYMBOL, OTHER, PUNCT_OR_SYMBOL
            - name: human-friendly name
            - pattern: regex fragment (without quantifier)
            - count: number of consecutive repeats
            - example_chars: list of chars covered
            - unicode_category (if detailed): Unicode category (e.g., 'Ll')
            - variant_matches (if detailed): List[str] of sample matches for this fragment
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    try:
        logger.info(f"Generating breakdown for: {text}")
        _, groups = _build_fragments_and_groups(text, use_char_map)
        breakdown = []
        for g in groups:
            item = {
                "type": g["type"],
                "name": g["name"],
                "pattern": g["pattern"],
                "count": g["count"],
                "example_chars": g.get("example_chars", [])
            }
            if detailed:
                # Add Unicode category for first char
                item["unicode_category"] = unicodedata.category(g["example_chars"][0]) if g["example_chars"] else "N/A"
                # Generate sample matches for this fragment
                try:
                    pat = g["pattern"] if g["count"] == 1 else f"(?:{g['pattern']}){{{g['count']}}}"
                    compiled = re.compile(pat)
                    variants = [c for c in g["example_chars"]]
                    for c in g["example_chars"]:
                        if c.lower() in char_map:
                            opts = re.findall(r'[a-zA-Z0-9]', char_map.get(c.lower(), c))
                            variants.extend(opts[:2])  # Limit to 2 variants
                    item["variant_matches"] = [v * g["count"] for v in variants[:3] if
                                               compiled.fullmatch(v * g["count"])]
                except re.error:
                    item["variant_matches"] = []
                logger.debug(f"Breakdown item: {item}")
            breakdown.append(item)

        logger.info(f"Generated breakdown with {len(breakdown)} items")
        return breakdown

    except Exception as e:
        logger.error(f"Error building breakdown: {e}")
        return [{"type": "ERROR", "name": f"error: {e}", "pattern": "", "count": 0, "example_chars": [],
                 "unicode_category": "N/A", "variant_matches": []} if detailed else
                {"type": "ERROR", "name": f"error: {e}", "pattern": "", "count": 0, "example_chars": []}]


def get_all_patterns() -> Dict[str, str]:
    """
    Returns a dictionary of all predefined regex patterns available in the library.
    Useful for copying or using in other functions.

    Returns:
        Dict[str, str]: Mapping of pattern names to regex patterns.
    """
    logger.info("Retrieving all predefined patterns")
    return PREDEFINED_PATTERNS.copy()