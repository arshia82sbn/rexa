# tests/test_regex_mapper.py

import pytest
import re
import unicodedata
from typing import List, Dict, Tuple
from rexa.regex_mapper import (
    string_to_regex,
    string_to_breakdown,
    get_all_patterns,
    char_map,
    PREDEFINED_PATTERNS
)
from utils.Logger import get_logger

logger = get_logger()

# Tests for string_to_regex
@pytest.mark.parametrize(
    ("text", "use_char_map", "use_anchors", "detailed", "expected"),
    [
        ("i'm", True, False, False, r"\b[iIíìîïİ1!|]['‘’][mM]\b"),
        ("good", True, True, False, r"^[gGğ9][oOóòôöõ0]{2}[dDđ]$"),
        ("123", False, False, False, r"\b\d{3}\b"),
        ("", True, False, False, r"\b\b"),
        # ("😊!", True, False, False, r"\b\U0001f60a[!1|I]\b"),
        ("i'm", True, False, True, lambda r: isinstance(r, tuple) and isinstance(r[1], dict) and r[1]["valid"]),
        ("invalid", True, False, True, lambda r: isinstance(r, tuple) and r[1]["valid"]),
    ],
)
def test_string_to_regex(text, use_char_map, use_anchors, detailed, expected):
    logger.debug(f"Testing string_to_regex with input: {text}")
    result = string_to_regex(text, use_char_map=use_char_map, use_anchors=use_anchors, detailed=detailed)
    if callable(expected):
        assert expected(result)
    else:
        assert result == expected
    if not detailed and text and not result.startswith("(Error"):
        assert re.fullmatch(result, text) is not None

# Tests for string_to_breakdown
@pytest.mark.parametrize(
    ("text", "use_char_map", "detailed", "expected_len"),
    [
        ("i'm", True, False, 3),
        ("good", True, True, 3),
        ("123", False, False, 1),
        ("", True, False, 0),
        # ("\U0001f60a!", True, True, 1),
    ],
)
def test_string_to_breakdown(text, use_char_map, detailed, expected_len):
    logger.debug(f"Testing string_to_breakdown with input: {text}")
    result = string_to_breakdown(text, use_char_map=use_char_map, detailed=detailed)
    assert len(result) == expected_len
    if result:
        assert all(isinstance(item, Dict) for item in result)
        assert all(key in item for item in result for key in ["type", "name", "pattern", "count", "example_chars"])
        if detailed:
            assert all("unicode_category" in item and "variant_matches" in item for item in result)
        reconstructed = "".join(item["pattern"] if item["count"] == 1 else f"(?:{item['pattern']}){{{item['count']}}}" for item in result)
        reconstructed = f"\\b{reconstructed}\\b"
        assert re.fullmatch(reconstructed, text) is not None

# Tests for get_all_patterns
def test_get_all_patterns():
    logger.debug("Testing get_all_patterns")
    result = get_all_patterns()
    assert isinstance(result, Dict)
    assert len(result) == 19
    assert "email" in result
    assert result["email"] == r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    assert re.fullmatch(result["email"], "user@example.com") is not None
    assert re.fullmatch(result["email"], "invalid") is None

# Tests for non-string inputs
def test_string_to_regex_non_string():
    logger.debug("Testing string_to_regex with non-string input")
    with pytest.raises(TypeError, match="Input must be a string"):
        string_to_regex(123)

def test_string_to_regex_detailed_non_string():
    logger.debug("Testing string_to_regex with non-string input and detailed=True")
    with pytest.raises(TypeError, match="Input must be a string"):
        string_to_regex(123, detailed=True)

def test_string_to_breakdown_non_string():
    logger.debug("Testing string_to_breakdown with non-string input")
    with pytest.raises(TypeError, match="Input must be a string"):
        string_to_breakdown(123)

# Tests for char_map and PREDEFINED_PATTERNS
def test_char_map():
    logger.debug("Testing char_map")
    assert isinstance(char_map, Dict)
    assert len(char_map) > 50
    assert 'a' in char_map
    assert re.fullmatch(char_map['a'], 'a') is not None
    assert re.fullmatch(char_map['a'], 'A') is not None
    assert re.fullmatch(char_map['a'], '@') is not None
    assert re.fullmatch(char_map['a'], '5') is None

def test_PREDEFINED_PATTERNS():
    logger.debug("Testing PREDEFINED_PATTERNS")
    assert isinstance(PREDEFINED_PATTERNS, Dict)
    assert len(PREDEFINED_PATTERNS) == 19  # Updated to match PREDEFINED_PATTERNS
    assert 'email' in PREDEFINED_PATTERNS
    assert re.fullmatch(PREDEFINED_PATTERNS['email'], "user@example.com") is not None
    assert re.fullmatch(PREDEFINED_PATTERNS['email'], "invalid") is None