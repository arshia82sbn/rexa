import re
from typing import Literal


class RexFormatter:
    """
    RexFormatter: A class that provides tools to clean and format strings
    such as removing HTML tags, normalizing spaces, dates, and more.
    """

    @staticmethod
    def Strip_HTMLTags(s: str, replace_with: str = '') -> str:
        """
        Remove all HTML tags from the string.

        Example: "<p>Hello <b>World</b></p>" → "Hello World"

        Parameters:
            s (str): Input string containing HTML.
            replace_with (str): Character(s) to replace the tags with. Default is empty.

        Returns:
            str: Cleaned string with HTML tags removed.
        """
        return re.sub(r'<[^>]*>', replace_with, s)

    @staticmethod
    def Normalize_Spaces(s: str) -> str:
        """
        Normalize all multiple spaces and tabs into a single space.

        Example: "This    is \t spaced" → "This is spaced"

        Parameters:
            s (str): Input string.

        Returns:
            str: Cleaned string with normalized spaces.
        """
        return re.sub(r'\s+', ' ', s).strip()

    @staticmethod
    def Remove_ThousandSeparators(s: str) -> str:
        """
        Remove thousands separators from numbers.

        Example: "1,234,567.89" → "1234567.89"

        Parameters:
            s (str): Input string.

        Returns:
            str: String without thousand separators.
        """
        return re.sub(r'(?<=\d),(?=\d{3}\b)', '', s)

    @staticmethod
    def Normalize_DateSeparator(s: str, sep: Literal['-', '/', '.'] = '-') -> str:
        """
        Normalize different date separators to a single consistent one.

        Example: "2025/08.02" → "2025-08-02"

        Parameters:
            s (str): Input string that may contain dates.
            sep (Literal['-', '/', '.']): Desired separator.

        Returns:
            str: String with normalized date separators.
        """
        return re.sub(r'[-/.]', sep, s)
