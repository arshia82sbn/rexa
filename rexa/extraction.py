import re
from typing import List

"""
RexExtractor: A utility class to extract specific patterns from raw text using regular expressions.

All methods return a list of matched strings.
"""


def Extract_Emails(text: str) -> List[str]:
    """
    Extract all email addresses from the given text.

    Parameters:
        text (str): Input string containing one or more email addresses.

    Returns:
        List[str]: A list of extracted email addresses.
    """
    pattern = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'


    return re.findall(pattern, text)


def Extract_URLs(text: str) -> List[str]:
    """
    Extract all URLs (http/https/ftp) from the given text.

    Parameters:
        text (str): Input string containing one or more URLs.

    Returns:
        List[str]: A list of extracted URLs.
    """
    pattern = r'\b(?:https?|ftp)://[^\s/$.?#].[^\s]*'
    return re.findall(pattern, text)


def Extract_Phones(text: str) -> List[str]:
    """
    Extract all phone numbers (Iranian and international) from the given text.

    Parameters:
        text (str): Input string that may include phone numbers.

    Returns:
        List[str]: A list of extracted phone numbers.
    """
    pattern = r'\+?\d[\d\s\-()]{7,}\d'
    return re.findall(pattern, text)


def Extract_Dates(text: str) -> List[str]:
    """
    Extract all date-like strings (ISO or common formats) from the given text.

    Parameters:
        text (str): Input string that may contain dates.

    Returns:
        List[str]: A list of extracted date strings.
    """
    pattern = r'\b(?:\d{4}[-/.]\d{2}[-/.]\d{2}|\d{2}[-/.]\d{2}[-/.]\d{4})\b'
    return re.findall(pattern, text)


def Extract_IPv4(text: str) -> List[str]:
    """
    Extract all IPv4 addresses from the given text.

    Parameters:
        text (str): Input string that may include IPv4 addresses.

    Returns:
        List[str]: A list of extracted IPv4 address strings.
    """
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.findall(pattern, text)


def Extract_UUIDs(text: str) -> List[str]:
    """
    Extract all UUIDv4 patterns from the given text.

    Parameters:
        text (str): Input string that may include UUIDs.

    Returns:
        List[str]: A list of extracted UUID strings.
    """
    text = text.lower()
    pattern = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    return re.findall(pattern, text)
