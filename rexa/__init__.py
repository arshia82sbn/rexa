from .conversion import (
    Convert_MultipleSpaces,
    Convert_ThousandSeparatedNumbers,
    Convert_DateFormat,
    Slugify
)

from .regex_mapper import (
    string_to_regex,
    string_to_breakdown,
    get_all_patterns
)

from .formatting import (
    Strip_HTMLTags,
    Normalize_Spaces,
    Remove_ThousandSeparators,
    Normalize_DateSeparator
)

from .validation import (
    Is_Email,
    Match_Email,
    Is_IranianPhone,
    Match_IranianPhone,
    Is_InternationalPhone,
    Match_InternationalPhone,
    Is_URL,
    Match_URL,
    Is_Date_ISO,
    Match_Date_ISO,
    Is_Date_EU,
    Match_Date_EU,
    Is_Time,
    Match_Time,
    Is_UUID4,
    Match_UUID4,
    Is_IranNationalCode,
    Match_IranNationalCode,
    Is_ISBN10,
    Match_ISBN10,
    Is_ISBN13,
    Match_ISBN13,
    Is_HexColor,
    Match_HexColor,
    Is_ScientificNumber,
    Match_ScientificNumber,
    Is_ThousandSepNumber,
    Match_ThousandSepNumber,
    Is_Mention,
    Match_Mention,
    Is_MarkdownLink,
    Match_MarkdownLink,
    Is_HTMLTag,
    Match_HTMLTag,
    Is_MultipleEmails,
    Match_MultipleEmails,
    Is_Base64,
    Match_Base64
)

from .texttools import (
    to_lower,
    to_upper,
    remove_emojis,
    remove_numbers,
    remove_usernames,
    remove_punctuation,
    remove_stopwords,
    lemmatize_text,
    stem_text,
    remove_urls_emails,
    normalize_whitespace,
    normalize_arabic,
    count_tokens,
    remove_short_long_words,
    detect_language,
    clean_text
)

from .extraction import (
    Extract_Emails,
    Extract_URLs,
    Extract_Phones,
    Extract_Dates,
    Extract_IPv4,
    Extract_UUIDs
)

from utils.Logger import get_logger

logger = get_logger()

logger.info("Rexa library initialized")
logger.debug("All methods imported successfully")