# tests/test_validation.py

import pytest
import re
from rexa.validation import (
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
from utils.Logger import get_logger

logger = get_logger()

# Tests for Email
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("user@example.com", True),
        ("user.name@sub.domain.co.uk", True),
        ("user+tag@example.com", True),
        ("invalid@", False),
        ("user@domain", False),
        ("", False),
    ],
)
def test_Is_Email(s, expected):
    logger.debug(f"Testing Is_Email with input: {s}")
    assert Is_Email(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("user@example.com", re.Match),
        ("invalid@", type(None)),
        ("", type(None)),
    ],
)
def test_Match_Email(s, expected_type):
    logger.debug(f"Testing Match_Email with input: {s}")
    assert isinstance(Match_Email(s), expected_type)

# Tests for IranianPhone
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("09121234567", True),
        ("+989121234567", True),
        ("00989121234567", True),
        ("0912123456", False),  # Too short
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_IranianPhone(s, expected):
    logger.debug(f"Testing Is_IranianPhone with input: {s}")
    assert Is_IranianPhone(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("09121234567", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_IranianPhone(s, expected_type):
    logger.debug(f"Testing Match_IranianPhone with input: {s}")
    assert isinstance(Match_IranianPhone(s), expected_type)

# Tests for InternationalPhone
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("+1234567890", True),
        ("1234567890", True),
        ("+1123456789012345", False),  # Max length
        ("+0123456789", False),  # Leading zero after +
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_InternationalPhone(s, expected):
    logger.debug(f"Testing Is_InternationalPhone with input: {s}")
    assert Is_InternationalPhone(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("+1234567890", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_InternationalPhone(s, expected_type):
    logger.debug(f"Testing Match_InternationalPhone with input: {s}")
    assert isinstance(Match_InternationalPhone(s), expected_type)

# Tests for URL
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("https://example.com", True),
        ("http://test.org/path", True),
        ("ftp://file.com", False),
        ("www.example.com", True),
        ("example.com", True),
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_URL(s, expected):
    logger.debug(f"Testing Is_URL with input: {s}")
    assert Is_URL(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("https://example.com", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_URL(s, expected_type):
    logger.debug(f"Testing Match_URL with input: {s}")
    assert isinstance(Match_URL(s), expected_type)

# Tests for Date_ISO
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("2024-09-29", True),
        ("2024-13-29", True),  # Invalid month but matches pattern
        ("2024-09-32", True),  # Invalid day but matches
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_Date_ISO(s, expected):
    logger.debug(f"Testing Is_Date_ISO with input: {s}")
    assert Is_Date_ISO(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("2024-09-29", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_Date_ISO(s, expected_type):
    logger.debug(f"Testing Match_Date_ISO with input: {s}")
    assert isinstance(Match_Date_ISO(s), expected_type)

# Tests for Date_EU
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("29/09/2024", True),
        ("32/09/2024", True),  # Invalid day but matches
        ("29/13/2024", True),  # Invalid month but matches
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_Date_EU(s, expected):
    logger.debug(f"Testing Is_Date_EU with input: {s}")
    assert Is_Date_EU(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("29/09/2024", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_Date_EU(s, expected_type):
    logger.debug(f"Testing Match_Date_EU with input: {s}")
    assert isinstance(Match_Date_EU(s), expected_type)

# Tests for Time
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("12:34:56", True),
        ("12:34", True),
        ("23:59:59", True),
        ("24:00", False),  # Invalid hour
        ("12:60", False),  # Invalid minute
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_Time(s, expected):
    logger.debug(f"Testing Is_Time with input: {s}")
    assert Is_Time(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("12:34:56", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_Time(s, expected_type):
    logger.debug(f"Testing Match_Time with input: {s}")
    assert isinstance(Match_Time(s), expected_type)

# Tests for UUID4
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("123e4567-e89b-12d3-a456-426614174000", False),
        ("a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11", True),
        ("123e4567-e89b-12d3-a456-42661417400", False),  # Too short
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_UUID4(s, expected):
    logger.debug(f"Testing Is_UUID4 with input: {s}")
    assert Is_UUID4(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("invalid", type(None)),
    ],
)
def test_Match_UUID4(s, expected_type):
    assert isinstance(Match_UUID4(s), expected_type)

# Tests for IranNationalCode
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("0012345678", True),
        ("1234567890", True),
        ("123456789", False),  # Too short
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_IranNationalCode(s, expected):
    logger.debug(f"Testing Is_IranNationalCode with input: {s}")
    assert Is_IranNationalCode(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("0012345678", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_IranNationalCode(s, expected_type):
    logger.debug(f"Testing Match_IranNationalCode with input: {s}")
    assert isinstance(Match_IranNationalCode(s), expected_type)

# Tests for ISBN10
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("123456789X", True),
        ("1234567890", True),
        ("123456789", False),  # Too short
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_ISBN10(s, expected):
    logger.debug(f"Testing Is_ISBN10 with input: {s}")
    assert Is_ISBN10(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("123456789X", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_ISBN10(s, expected_type):
    logger.debug(f"Testing Match_ISBN10 with input: {s}")
    assert isinstance(Match_ISBN10(s), expected_type)

# Tests for ISBN13
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("9781234567890", True),
        ("1234567890123", True),
        ("123456789012", False),  # Too short
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_ISBN13(s, expected):
    logger.debug(f"Testing Is_ISBN13 with input: {s}")
    assert Is_ISBN13(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("9781234567890", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_ISBN13(s, expected_type):
    logger.debug(f"Testing Match_ISBN13 with input: {s}")
    assert isinstance(Match_ISBN13(s), expected_type)

# Tests for HexColor
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("#FFFFFF", True),
        ("#FFF", True),
        ("#ffffff", True),
        ("#fff", True),
        ("#FFFFFG", False),  # Invalid hex
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_HexColor(s, expected):
    logger.debug(f"Testing Is_HexColor with input: {s}")
    assert Is_HexColor(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("#FFFFFF", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_HexColor(s, expected_type):
    logger.debug(f"Testing Match_HexColor with input: {s}")
    assert isinstance(Match_HexColor(s), expected_type)

# Tests for ScientificNumber
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("1.23e4", True),
        ("-4.56E-7", True),
        (".789e10", True),
        ("1e4", True),
        ("1.23e", False),  # Incomplete
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_ScientificNumber(s, expected):
    logger.debug(f"Testing Is_ScientificNumber with input: {s}")
    assert Is_ScientificNumber(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("1.23e4", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_ScientificNumber(s, expected_type):
    logger.debug(f"Testing Match_ScientificNumber with input: {s}")
    assert isinstance(Match_ScientificNumber(s), expected_type)

# Tests for ThousandSepNumber
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("1,234,567", True),
        ("1234.56", False),
        ("1,234.56", True),
        ("12,34,567", False),  # Invalid grouping
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_ThousandSepNumber(s, expected):
    logger.debug(f"Testing Is_ThousandSepNumber with input: {s}")
    assert Is_ThousandSepNumber(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("1,234,567", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_ThousandSepNumber(s, expected_type):
    logger.debug(f"Testing Match_ThousandSepNumber with input: {s}")
    assert isinstance(Match_ThousandSepNumber(s), expected_type)

# Tests for Mention
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("@user", True),
        ("@User_123", True),
        ("@invalid!", False),
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_Mention(s, expected):
    logger.debug(f"Testing Is_Mention with input: {s}")
    assert Is_Mention(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("@user", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_Mention(s, expected_type):
    logger.debug(f"Testing Match_Mention with input: {s}")
    assert isinstance(Match_Mention(s), expected_type)

# Tests for MarkdownLink
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("[link](https://example.com)", True),
        ("[text](url)", True),
        ("[invalid](", False),
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_MarkdownLink(s, expected):
    logger.debug(f"Testing Is_MarkdownLink with input: {s}")
    assert Is_MarkdownLink(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("[link](url)", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_MarkdownLink(s, expected_type):
    logger.debug(f"Testing Match_MarkdownLink with input: {s}")
    assert isinstance(Match_MarkdownLink(s), expected_type)

# Tests for HTMLTag
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("<tag>", True),
        ("<tag attr='value'>", True),
        ("<tag />", True),
        ("<invalid", False),
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_HTMLTag(s, expected):
    logger.debug(f"Testing Is_HTMLTag with input: {s}")
    assert Is_HTMLTag(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("<tag>", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_HTMLTag(s, expected_type):
    logger.debug(f"Testing Match_HTMLTag with input: {s}")
    assert isinstance(Match_HTMLTag(s), expected_type)

# Tests for MultipleEmails
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("email1@example.com, email2@example.com", True),
        ("single@example.com", True),
        ("invalid", False),
        ("", False),
    ],
)
def test_Is_MultipleEmails(s, expected):
    logger.debug(f"Testing Is_MultipleEmails with input: {s}")
    assert Is_MultipleEmails(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("email1@example.com, email2@example.com", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_MultipleEmails(s, expected_type):
    logger.debug(f"Testing Match_MultipleEmails with input: {s}")
    assert isinstance(Match_MultipleEmails(s), expected_type)

# Tests for Base64
@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("YWJj", True),  # 'abc' in base64
        ("YWJjZA==", True),
        ("YWJjZ==", False),  # Padding
        ("invalid!", False),
        ("", True),
    ],
)
def test_Is_Base64(s, expected):
    logger.debug(f"Testing Is_Base64 with input: {s}")
    assert Is_Base64(s) == expected

@pytest.mark.parametrize(
    ("s", "expected_type"),
    [
        ("YWJj", re.Match),
        ("invalid", type(None)),
    ],
)
def test_Match_Base64(s, expected_type):
    logger.debug(f"Testing Match_Base64 with input: {s}")
    assert isinstance(Match_Base64(s), expected_type)