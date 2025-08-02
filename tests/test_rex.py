# tests/test_rex.py

import pytest
from rexa import Rex

@pytest.fixture
def rex():
    """Provide a fresh Rex instance for each test."""
    return Rex()

# ——————— Validation & Matching ———————

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("user@example.com", True),
        ("bad-email@", False),
        ("another.user@sub.domain.org", True),
        ("no_at_symbol.com", False),
    ],
)
def test_Is_Email(rex, input_str, expected):
    assert rex.validator.Is_Email(input_str) is expected

def test_Match_Email_groups(rex):
    m = rex.validator.Match_Email("user@domain.com")
    assert m is not None
    assert m.group(0) == "user@domain.com"
    assert rex.validator.Match_Email("invalid@") is None

# ——————— Extraction ———————

def test_Extract_Emails(rex):
    text = "Contact: alice@example.com, bob@test.org; carol@domain.net"
    out = rex.extractor.Extract_Emails(text)
    assert isinstance(out, list)
    assert sorted(out) == ["alice@example.com", "bob@test.org", "carol@domain.net"]

# ——————— Conversion ———————

@pytest.mark.parametrize(
    ("input_text", "expected"),
    [
        ("This   has   extra   spaces", "This has extra spaces"),
        ("Leading and trailing   ", "Leading and trailing"),
    ],
)
def test_Convert_MultipleSpaces(rex, input_text, expected):
    assert rex.converter.Convert_MultipleSpaces(input_text) == expected

def test_Convert_ThousandSeparatedNumbers(rex):
    input_text = "Population: 1,234,567 people"
    assert rex.converter.Convert_ThousandSeparatedNumbers(input_text) == "Population: 1234567 people"

@pytest.mark.parametrize(
    ("date_str", "current_sep", "target_sep", "expected"),
    [
        ("2025-08-02", "-", "/", "2025/08/02"),
        ("01.12.2024", ".", "-", "01-12-2024"),
        ("wrongformat", "-", "/", None),
    ],
)
def test_Convert_DateFormat(rex, date_str, current_sep, target_sep, expected):
    assert rex.converter.Convert_DateFormat(date_str, current_sep, target_sep) == expected

def test_Slugify(rex):
    assert rex.converter.Slugify("Hello, World!") == "hello-world"
    assert rex.converter.Slugify("  Clean__this__Up  ") == "clean-this-up"

# ——————— Formatting & Cleanup ———————

def test_Strip_HTMLTags(rex):
    html = "<div><p>Text <b>bold</b></p></div>"
    assert rex.formatter.Strip_HTMLTags(html) == "Text bold"

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        ("A    B\tC\n\nD", "A B C D"),
        (" No   extra spaces ", "No extra spaces"),
    ],
)
def test_Normalize_Spaces(rex, input_str, expected):
    assert rex.formatter.Normalize_Spaces(input_str) == expected

def test_Remove_ThousandSeparators(rex):
    assert rex.formatter.Remove_ThousandSeparators("Value: 9,876,543.21") == "Value: 9876543.21"

@pytest.mark.parametrize(
    ("input_str", "sep", "expected"),
    [
        ("2025/08.02", "-", "2025-08-02"),
        ("01.01.2023", "/", "01/01/2023"),
    ],
)
def test_Normalize_DateSeparator(rex, input_str, sep, expected):
    assert rex.formatter.Normalize_DateSeparator(input_str, sep) == expected
