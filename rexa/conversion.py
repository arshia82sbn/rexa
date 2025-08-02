import re
from typing import Optional
from datetime import datetime


class RexConverter:
    """
    RexConverter: A class for converting raw text formats to more usable or standardized forms.
    """

    @staticmethod
    def Convert_MultipleSpaces(text: str) -> str:
        """
        Convert multiple consecutive spaces to a single space.

        Example: "This   is   spaced" → "This is spaced"

        Parameters:
            text (str): Input string.

        Returns:
            str: Cleaned string with single spaces.
        """
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def Convert_ThousandSeparatedNumbers(text: str) -> str:
        """
        Convert numbers with comma separators into plain numbers.

        Example: "The number is 1,234,567." → "The number is 1234567."

        Parameters:
            text (str): Input string.

        Returns:
            str: String with comma-separated numbers converted to plain form.
        """
        return re.sub(r'(?<=\d),(?=\d{3}\b)', '', text)

    @staticmethod
    def Convert_DateFormat(date_str: str, current_sep: str = '-', target_sep: str = '/') -> Optional[str]:
        """
        Convert date string from one separator to another.
        Example: "2025-08-02" → "2025/08/02"

        Parameters:
            date_str (str): Original date string.
            current_sep (str): Current separator used in the date (e.g., '-').
            target_sep (str): Desired separator (e.g., '/').

        Returns:
            Optional[str]: Reformatted date string or None if invalid.
        """
        try:
            parts = date_str.split(current_sep)
            if len(parts) == 3:
                return target_sep.join(parts)
        except Exception:
            return None
        return None

    @staticmethod
    def Slugify(text: str) -> str:
        """
        Convert a given string into a slug usable in URLs.

        Example: "Hello World!" → "hello-world"

        Parameters:
            text (str): Input string.

        Returns:
            str: Slugified string.
        """
        # Remove special characters
        text = re.sub(r'[^\w\s-]', '', text)
        # Replace whitespace and underscores with hyphens
        text = re.sub(r'[\s_]+', '-', text)
        return text.strip('-').lower()
