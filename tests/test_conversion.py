# tests/test_conversion.py

import pytest
import re
from rexa.conversion import (
    Convert_MultipleSpaces,
    Convert_ThousandSeparatedNumbers,
    Convert_DateFormat,
    Slugify
)
from utils.Logger import get_logger

logger = get_logger()

# Tests for Convert_MultipleSpaces
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("This   is   spaced", "This is spaced"),
        ("", ""),
        ("\n\t  Multiple   spaces  ", "Multiple spaces"),
        ("Single", "Single"),
        ("   Leading trailing   ", "Leading trailing"),
        ("\t\n\r", ""),  # Only whitespace
    ],
)
def test_Convert_MultipleSpaces(text, expected):
    logger.debug(f"Testing Convert_MultipleSpaces with input: {text}")
    assert Convert_MultipleSpaces(text) == expected

# Tests for Convert_ThousandSeparatedNumbers
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("1,234,567", "1234567"),
        ("No commas", "No commas"),
        ("", ""),
        ("1,000.50", "1000.50"),
        ("12,34,567", "1234567"),  # Invalid thousand separator
        ("1,234,567.89", "1234567.89"),
    ],
)
def test_Convert_ThousandSeparatedNumbers(text, expected):
    logger.debug(f"Testing Convert_ThousandSeparatedNumbers with input: {text}")
    assert Convert_ThousandSeparatedNumbers(text) == expected

# Tests for Convert_DateFormat
@pytest.mark.parametrize(
    ("date_str", "current_sep", "target_sep", "expected"),
    [
        ("2025-08-02", "-", "/", "2025/08/02"),
        ("2025.08.02", ".", "-", "2025-08-02"),
        ("invalid", "-", "/", None),
        ("", "-", "/", None),
        ("2025/08/02", "/", ".", "2025.08.02"),
        ("2025-08", "-", "/", None),  # Incomplete date
        ("2025--08--02", "-", "/", "2025/08/02"),  # Multiple separators
    ],
)
def test_Convert_DateFormat(date_str, current_sep, target_sep, expected):
    logger.debug(f"Testing Convert_DateFormat with input: {date_str}")
    assert Convert_DateFormat(date_str, current_sep, target_sep) == expected

# Tests for Slugify
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello World!", "hello-world"),
        ("", ""),
        ("This is a TEST!", "this-is-a-test"),
        ("Special@#$Chars", "special-chars"),
        ("  Spaces  Around  ", "spaces-around"),
        ("Under_score", "under-score"),  # Updated expectation
        ("-Leading-Trailing-", "leading-trailing"),
    ],
)
def test_Slugify(text, expected):
    logger.debug(f"Testing Slugify with input: {text}")
    assert Slugify(text) == expected