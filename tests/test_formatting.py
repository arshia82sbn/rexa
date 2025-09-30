# tests/test_formatting.py

import pytest
import re
from rexa.formatting import (
    Strip_HTMLTags,
    Normalize_Spaces,
    Remove_ThousandSeparators,
    Normalize_DateSeparator
)
from utils.Logger import get_logger

logger = get_logger()

# Tests for Strip_HTMLTags
@pytest.mark.parametrize(
    ("s", "replace_with", "expected"),
    [
        ("<p>Hello <b>World</b></p>", "", "Hello World"),
        ("<div>Content</div>", " ", " Content "),
        ("", "", ""),
        ("<script>alert('xss')</script>", "", "alert('xss')"),
        ("No tags here", "", "No tags here"),
        ("<p>Nested <span>tags</span> here</p>", "-", '-Nested -tags- here-'),
        ("<br />", "", ""),  # Self-closing tag
        ("Incomplete <tag", "", "Incomplete "),  # Malformed tag
    ],
)
def test_Strip_HTMLTags(s, replace_with, expected):
    logger.debug(f"Testing Strip_HTMLTags with input: {s}")
    assert Strip_HTMLTags(s, replace_with) == expected

# Tests for Normalize_Spaces
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("This    is \t spaced", "This is spaced"),
        (" No spaces ", "No spaces"),
        ("", ""),
        ("\n\t\r", ""),
        ("Single", "Single"),
        ("  Multiple   spaces  ", "Multiple spaces"),
        ("\t\n   Mixed\twhitespace  ", "Mixed whitespace"),
    ],
)
def test_Normalize_Spaces(s, expected):
    logger.debug(f"Testing Normalize_Spaces with input: {s}")
    assert Normalize_Spaces(s) == expected

# Tests for Remove_ThousandSeparators
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("1,234,567.89", "1234567.89"),
        ("No numbers", "No numbers"),
        ("", ""),
        ("1,000", "1000"),
        ("12,34,567", "1234567"),  # Invalid thousand separator
        ("1,234.56", "1234.56"),
        ("1,234,56", "123456"),  # Invalid format
    ],
)
def test_Remove_ThousandSeparators(s, expected):
    logger.debug(f"Testing Remove_ThousandSeparators with input: {s}")
    assert Remove_ThousandSeparators(s) == expected

# Tests for Normalize_DateSeparator
@pytest.mark.parametrize(
    ("s", "sep", "expected"),
    [
        ("2025/08.02", "-", "2025-08-02"),
        ("2025-08-02", "/", "2025/08/02"),
        ("", "-", ""),
        ("2025.08.02", "-", "2025-08-02"),
        ("2025/08/02", ".", "2025.08.02"),
        ("No date", "-", "No date"),
        ("2025--08--02", "-", "2025--08--02"),  # Multiple separators
    ],
)
def test_Normalize_DateSeparator(s, sep, expected):
    logger.debug(f"Testing Normalize_DateSeparator with input: {s}")
    assert Normalize_DateSeparator(s, sep) == expected