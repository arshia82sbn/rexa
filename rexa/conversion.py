# rexa/conversion.py

import re
from utils.Logger import get_logger

logger = get_logger()

"""
RexConverter: A class for converting raw text formats to more usable or standardized forms.
"""

def Convert_MultipleSpaces(text: str) -> str:
    """
    Convert multiple consecutive spaces into a single space.

    Args:
        text (str): Input text with multiple spaces.

    Returns:
        str: Text with multiple spaces converted to single spaces.
    """
    return re.sub(r'\s+', ' ', text).strip()


def Convert_ThousandSeparatedNumbers(text: str) -> str:
    """
    Remove thousand separators (commas) from numbers in the format like 1,234,567.

    Args:
        text (str): Input text containing numbers with thousand separators.

    Returns:
        str: Text with thousand separators removed from valid numbers.
    """
    pattern = r'\b\d[\d,]*(?:\.\d+)?\b'

    def remove_commas(match):
        return match.group(0).replace(',', '')

    return re.sub(pattern, remove_commas, text)


def Convert_DateFormat(date_str: str, current_sep: str, target_sep: str) -> str:
    """
    Convert date format by changing the separator (e.g., from '-' to '/').

    Args:
        date_str (str): Input date string (e.g., '2025-08-02').
        current_sep (str): Current separator (e.g., '-').
        target_sep (str): Target separator (e.g., '/').

    Returns:
        str: Converted date string or None if invalid.
    """
    try:
        # Collapse multiple consecutive separators into one
        escaped_sep = re.escape(current_sep)
        date_str = re.sub(rf'{escaped_sep}+', current_sep, date_str)
        parts = date_str.split(current_sep)
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            return f"{parts[0]}{target_sep}{parts[1]}{target_sep}{parts[2]}"
        return None
    except:
        return None


def Slugify(text: str) -> str:
    """
    Convert text to a slug (lowercase, hyphen-separated, no special characters).

    Args:
        text (str): Input text to slugify.

    Returns:
        str: Slugified text.
    """
    if not text:
        return ""
    # Convert to lowercase
    text = text.lower()
    print(text)
    # Replace spaces, underscores, and special characters with hyphens
    text = re.sub(r'[\s_]+|[^a-z0-9-]', '-', text)
    print(text)
    # Remove multiple consecutive hyphens
    text = re.sub(r'-+', '-', text)
    print(text)
    # Remove leading/trailing hyphens
    return text.strip('-')