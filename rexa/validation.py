import re
from typing import Optional, Match

"""
Validator provides methods to validate or match strings against common patterns
such as email, phone numbers, URLs, dates, UUIDs, etc.
Each pattern has two methods:
  - Is_<Name>(s: str) -> bool        : returns True/False if full string matches.
  - Match_<Name>(s: str) -> Match|None: returns the Match object if full match, else None.
"""

def Is_Email( s: str) -> bool:
    """
    Check if the entire string is a valid email address.

    Parameters:
        s (str): Input string to validate as email.

    Returns:
        bool: True if `s` is a valid email, False otherwise.
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(pattern, s) is not None

def Match_Email( s: str) -> Optional[Match]:
    """
    Attempt to match the entire string as an email address.

    Parameters:
        s (str): Input string to match.

    Returns:
        Optional[Match]: The match object if `s` is a valid email, else None.
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(pattern, s)

def Is_IranianPhone( s: str) -> bool:
    """
    Check if the string is an Iranian mobile phone number.
    Accepts formats like '09121234567', '+989121234567', or '00989121234567'.

    Parameters:
        s (str): Input phone string.

    Returns:
        bool: True if valid Iranian mobile, False otherwise.
    """
    pattern = r'^(?:00989|\+989|09)[0-9]{9}$'
    return re.fullmatch(pattern, s) is not None

def Match_IranianPhone( s: str) -> Optional[Match]:
    """
    Match an Iranian mobile phone number.

    Parameters:
        s (str): Input phone string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^(?:00989|\+989|09)[0-9]{9}$'
    return re.fullmatch(pattern, s)

def Is_InternationalPhone( s: str) -> bool:
    """
    Check if the string is an international phone number in E.164 format.
    E.g. '+123456789012', no spaces or punctuation.

    Parameters:
        s (str): Input phone string.

    Returns:
        bool: True if valid E.164 phone, False otherwise.
    """
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.fullmatch(pattern, s) is not None

def Match_InternationalPhone( s: str) -> Optional[Match]:
    """
    Match an international E.164 phone number.

    Parameters:
        s (str): Input phone string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.fullmatch(pattern, s)

def Is_URL( s: str) -> bool:
    """
    Check if the string is a valid HTTP/HTTPS URL.

    Parameters:
        s (str): Input URL string.

    Returns:
        bool: True if valid URL, False otherwise.
    """
    pattern = (
        r'^(?:https?://)?'            # optional http:// or https://
        r'(?:www\.)?'                 # optional www.
        r'[A-Za-z0-9.-]+'             # domain name
        r'\.[A-Za-z]{2,}'             # top-level domain
        r'(?:/[^\s]*)?$'              # optional path/query
    )
    return re.fullmatch(pattern, s) is not None

def Match_URL( s: str) -> Optional[Match]:
    """
    Match a valid HTTP/HTTPS URL.

    Parameters:
        s (str): Input URL string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = (
        r'^(?:https?://)?'
        r'(?:www\.)?'
        r'[A-Za-z0-9.-]+'
        r'\.[A-Za-z]{2,}'
        r'(?:/[^\s]*)?$'
    )
    return re.fullmatch(pattern, s)

def Is_Date_ISO( s: str) -> bool:
    """
    Check if the string is a date in ISO format YYYY-MM-DD.

    Parameters:
        s (str): Input date string.

    Returns:
        bool: True if matches ISO format, False otherwise.
    """
    pattern = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
    return re.fullmatch(pattern, s) is not None

def Match_Date_ISO( s: str) -> Optional[Match]:
    """
    Match an ISO date (YYYY-MM-DD).

    Parameters:
        s (str): Input date string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$'
    return re.fullmatch(pattern, s)

def Is_Date_EU( s: str) -> bool:
    """
    Check if the string is a European-style date DD/MM/YYYY.

    Parameters:
        s (str): Input date string.

    Returns:
        bool: True if matches DD/MM/YYYY, False otherwise.
    """
    pattern = r'^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$'
    return re.fullmatch(pattern, s) is not None

def Match_Date_EU( s: str) -> Optional[Match]:
    """
    Match a European-style date DD/MM/YYYY.

    Parameters:
        s (str): Input date string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-3][0-9]/[0-1][0-9]/[0-9]{4}$'
    return re.fullmatch(pattern, s)

def Is_Time( s: str) -> bool:
    """
    Check if the string is a time in HH:MM or HH:MM:SS (24-hour).

    Parameters:
        s (str): Input time string.

    Returns:
        bool: True if valid time, False otherwise.
    """
    pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?$'
    return re.fullmatch(pattern, s) is not None

def Match_Time( s: str) -> Optional[Match]:
    """
    Match a time string in 24-hour format.

    Parameters:
        s (str): Input time string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^(?:[01]\d|2[0-3]):[0-5]\d(?::[0-5]\d)?$'
    return re.fullmatch(pattern, s)

def Is_UUID4( s: str) -> bool:
    """
    Check if the string is a valid UUID version 4.

    Parameters:
        s (str): Input UUID string.

    Returns:
        bool: True if valid UUID4, False otherwise.
    """
    pattern = (
        r'^[0-9a-fA-F]{8}-'
        r'[0-9a-fA-F]{4}-'
        r'4[0-9a-fA-F]{3}-'
        r'[89ABab][0-9a-fA-F]{3}-'
        r'[0-9a-fA-F]{12}$'
    )
    return re.fullmatch(pattern, s) is not None

UUID4_REGEX = re.compile(
    r"^[0-9a-f]{8}-"      # 8 hex digits
    r"[0-9a-f]{4}-"       # 4 hex digits
    r"4[0-9a-f]{3}-"      # 4 indicates UUID version 4
    r"[89ab][0-9a-f]{3}-" # variant 1 (8,9,a,b)
    r"[0-9a-f]{12}$",     # 12 hex digits
    re.IGNORECASE
)

def Match_UUID4(s: str):
    """
    Returns a re.Match object if s is a valid UUID4 string,
    otherwise returns None.
    """
    return UUID4_REGEX.match(s)


def Is_IranNationalCode( s: str) -> bool:
    """
    Check if the string is a 10-digit Iranian national code.
    (No checksum logic, just pattern.)

    Parameters:
        s (str): Input national code.

    Returns:
        bool: True if exactly 10 digits, False otherwise.
    """
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, s) is not None

def Match_IranNationalCode( s: str) -> Optional[Match]:
    """
    Match an Iranian national code.

    Parameters:
        s (str): Input national code.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, s)

def Is_CreditCard16( s: str) -> bool:
    """
    Check if the string is a 16-digit credit card number.

    Parameters:
        s (str): Input card number.

    Returns:
        bool: True if exactly 16 digits, False otherwise.
    """
    pattern = r'^[0-9]{16}$'
    return re.fullmatch(pattern, s) is not None

def Match_CreditCard16( s: str) -> Optional[Match]:
    """
    Match a 16-digit credit card number.

    Parameters:
        s (str): Input card number.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{16}$'
    return re.fullmatch(pattern, s)

def Is_IranPostalCode( s: str) -> bool:
    """
    Check if the string is a 10-digit Iranian postal code.

    Parameters:
        s (str): Input postal code.

    Returns:
        bool: True if exactly 10 digits, False otherwise.
    """
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, s) is not None

def Match_IranPostalCode( s: str) -> Optional[Match]:
    """
    Match an Iranian postal code.

    Parameters:
        s (str): Input postal code.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, s)

def Is_USAZip( s: str) -> bool:
    """
    Check if the string is a US ZIP code (5 or 5+4 digits).

    Parameters:
        s (str): Input ZIP code.

    Returns:
        bool: True if valid (e.g. '12345' or '12345-6789'), False otherwise.
    """
    pattern = r'^[0-9]{5}(?:-[0-9]{4})?$'
    return re.fullmatch(pattern, s) is not None

def Match_USAZip( s: str) -> Optional[Match]:
    """
    Match a US ZIP code.

    Parameters:
        s (str): Input ZIP code.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{5}(?:-[0-9]{4})?$'
    return re.fullmatch(pattern, s)

def Is_ISBN10( s: str) -> bool:
    """
    Check if the string is a valid ISBN-10 (digits or final 'X').

    Parameters:
        s (str): Input ISBN-10.

    Returns:
        bool: True if matches ISBN-10 pattern, False otherwise.
    """
    pattern = r'^(?:\d{9}X|\d{10})$'
    return re.fullmatch(pattern, s) is not None

def Match_ISBN10( s: str) -> Optional[Match]:
    """
    Match an ISBN-10 code.

    Parameters:
        s (str): Input ISBN-10.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^(?:\d{9}X|\d{10})$'
    return re.fullmatch(pattern, s)

def Is_ISBN13( s: str) -> bool:
    """
    Check if the string is a 13-digit ISBN-13.

    Parameters:
        s (str): Input ISBN-13.

    Returns:
        bool: True if exactly 13 digits, False otherwise.
    """
    pattern = r'^[0-9]{13}$'
    return re.fullmatch(pattern, s) is not None

def Match_ISBN13( s: str) -> Optional[Match]:
    """
    Match an ISBN-13 code.

    Parameters:
        s (str): Input ISBN-13.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{13}$'
    return re.fullmatch(pattern, s)

def Is_HexColor( s: str) -> bool:
    """
    Check if the string is a hex color code (#RGB or #RRGGBB).

    Parameters:
        s (str): Input color code.

    Returns:
        bool: True if valid hex color, False otherwise.
    """
    pattern = r'^#(?:[0-9A-Fa-f]{3}){1,2}$'
    return re.fullmatch(pattern, s) is not None

def Match_HexColor( s: str) -> Optional[Match]:
    """
    Match a hex color code (#RGB or #RRGGBB).

    Parameters:
        s (str): Input color code.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^#(?:[0-9A-Fa-f]{3}){1,2}$'
    return re.fullmatch(pattern, s)

def Is_ScientificNumber( s: str) -> bool:
    """
    Check if the string is a scientific notation number (e.g. 1.23e+10).

    Parameters:
        s (str): Input number string.

    Returns:
        bool: True if matches scientific notation, False otherwise.
    """
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)$'
    return re.fullmatch(pattern, s) is not None

def Match_ScientificNumber( s: str) -> Optional[Match]:
    """
    Match a scientific notation number.

    Parameters:
        s (str): Input number string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)$'
    return re.fullmatch(pattern, s)

def Is_ThousandSepNumber( s: str) -> bool:
    """
    Check if the string is a number with thousand separators (e.g. 1,234,567).

    Parameters:
        s (str): Input number string.

    Returns:
        bool: True if valid format, False otherwise.
    """
    pattern = r'^[0-9]{1,3}(?:,[0-9]{3})*(?:\.\d+)?$'
    return re.fullmatch(pattern, s) is not None

def Match_ThousandSepNumber( s: str) -> Optional[Match]:
    """
    Match a number with thousand separators.

    Parameters:
        s (str): Input number string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^[0-9]{1,3}(?:,[0-9]{3})*(?:\.\d+)?$'
    return re.fullmatch(pattern, s)

def Is_Mention( s: str) -> bool:
    """
    Check if the string is a social-media mention (e.g. @username).

    Parameters:
        s (str): Input mention string.

    Returns:
        bool: True if matches mention pattern, False otherwise.
    """
    pattern = r'^@[A-Za-z0-9_]+$'
    return re.fullmatch(pattern, s) is not None

def Match_Mention( s: str) -> Optional[Match]:
    """
    Match a social-media mention.

    Parameters:
        s (str): Input mention string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^@[A-Za-z0-9_]+$'
    return re.fullmatch(pattern, s)

def Is_MarkdownLink( s: str) -> bool:
    """
    Check if the string is a Markdown link [text](url).

    Parameters:
        s (str): Input Markdown link.

    Returns:
        bool: True if valid link, False otherwise.
    """
    pattern = r'^\[.+?\]\([^)]+\)$'
    return re.fullmatch(pattern, s) is not None

def Match_MarkdownLink( s: str) -> Optional[Match]:
    """
    Match a Markdown-style link.

    Parameters:
        s (str): Input Markdown link.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^\[.+?\]\([^)]+\)$'
    return re.fullmatch(pattern, s)

def Is_HTMLTag( s: str) -> bool:
    """
    Check if the string is a single HTML tag (opening or closing).

    Parameters:
        s (str): Input HTML tag.

    Returns:
        bool: True if valid HTML tag syntax, False otherwise.
    """
    pattern = r'^<[^>]+>$'
    return re.fullmatch(pattern, s) is not None

def Match_HTMLTag( s: str) -> Optional[Match]:
    """
    Match a single HTML tag.

    Parameters:
        s (str): Input HTML tag.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^<[^>]+>$'
    return re.fullmatch(pattern, s)

def Is_MultipleEmails( s: str) -> bool:
    """
    Check if the string is one or more comma-separated email addresses.

    Parameters:
        s (str): Input string with emails separated by commas.

    Returns:
        bool: True if all items are valid emails, False otherwise.
    """
    pattern = (
        r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        r'(?:\s*,\s*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})*$'
    )
    return re.fullmatch(pattern, s) is not None

def Match_MultipleEmails( s: str) -> Optional[Match]:
    """
    Match a comma-separated list of email addresses.

    Parameters:
        s (str): Input string with emails separated by commas.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = (
        r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
        r'(?:\s*,\s*[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})*$'
    )
    return re.fullmatch(pattern, s)

def Is_Base64( s: str) -> bool:
    """
    Check if the string is valid Base64-encoded data.

    Parameters:
        s (str): Input Base64 string.

    Returns:
        bool: True if valid Base64 format, False otherwise.
    """
    pattern = r'^(?:[A-Za-z0-9+/]{4})*' \
              r'(?:[A-Za-z0-9+/]{2}==|' \
              r'[A-Za-z0-9+/]{3}=)?$'
    return re.fullmatch(pattern, s) is not None

def Match_Base64( s: str) -> Optional[Match]:
    """
    Match a Base64-encoded string.

    Parameters:
        s (str): Input Base64 string.

    Returns:
        Optional[Match]: Match object if valid, else None.
    """
    pattern = r'^(?:[A-Za-z0-9+/]{4})*' \
              r'(?:[A-Za-z0-9+/]{2}==|' \
              r'[A-Za-z0-9+/]{3}=)?$'
    return re.fullmatch(pattern, s)
