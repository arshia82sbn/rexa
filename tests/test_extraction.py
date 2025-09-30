# tests/test_extraction.py

import pytest
from rexa.extraction import (
    Extract_Emails,
    Extract_URLs,
    Extract_Phones,
    Extract_Dates,
    Extract_IPv4,
    Extract_UUIDs
)
from utils.Logger import get_logger

logger = get_logger()

# Tests for Extract_Emails
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Contact: alice@example.com, bob@test.org; carol@domain.net", ["alice@example.com", "bob@test.org", "carol@domain.net"]),
        ("No emails here", []),
        ("", []),
        ("user+tag@example.com", ["tag@example.com"]),
        ("user.name@sub.domain.co.uk", ["user.name@sub.domain.co.uk"]),
        ("email with space@example.com", ["space@example.com"]),  # Invalid
    ],
)
def test_Extract_Emails(text, expected):
    logger.debug(f"Testing Extract_Emails with input: {text}")
    result = Extract_Emails(text)
    assert sorted(result) == sorted(expected)

# Tests for Extract_URLs
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Visit https://example.com and http://test.org", ["https://example.com", "http://test.org"]),
        ("No URLs", []),
        ("", []),
        ("ftp://file.com/path", ["ftp://file.com/path"]),
        ("https://x.com with space", ["https://x.com"]),
        ("http://example.com/path?query=1#fragment", ["http://example.com/path?query=1#fragment"]),
        ("www.example.com", []),  # No protocol
        ("https://example.com:8080", ["https://example.com:8080"]),
    ],
)
def test_Extract_URLs(text, expected):
    logger.debug(f"Testing Extract_URLs with input: {text}")
    result = Extract_URLs(text)
    assert sorted(result) == sorted(expected)

# Tests for Extract_Phones
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Call +123456789 or 09121234567", ["+123456789", "09121234567"]),
        ("No phones", []),
        ("", []),
        ("(123) 456-7890", ["123) 456-7890"]),
        ("+98 912 123 4567", ["+98 912 123 4567"]),
        ("123-4567", []),  # Too short
        ("+1 (800) 555-1234", ["+1 (800) 555-1234"]),
        ("phone: 123456789012345", ["123456789012345"]),  # Long international
    ],
)
def test_Extract_Phones(text, expected):
    logger.debug(f"Testing Extract_Phones with input: {text}")
    result = Extract_Phones(text)
    assert sorted(result) == sorted(expected)

# Tests for Extract_Dates
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Dates: 2024-09-29 and 29/09/2024", ["2024-09-29", "29/09/2024"]),
        ("No dates", []),
        ("", []),
        ("2024.09.29", ["2024.09.29"]),
        ("01-01-2024", ["01-01-2024"]),
        ("99/99/9999", ["99/99/9999"]),
        ("2024-13-29", ["2024-13-29"]),  # Invalid date but matches pattern
        ("2024-09-29T10:00", []),  # Timestamp not matched
    ],
)
def test_Extract_Dates(text, expected):
    logger.debug(f"Testing Extract_Dates with input: {text}")
    result = Extract_Dates(text)
    assert sorted(result) == sorted(expected)

# Tests for Extract_IPv4
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("IPs: 192.168.1.1, 10.0.0.1", ["192.168.1.1", "10.0.0.1"]),
        ("No IPs", []),
        ("", []),
        ("255.255.255.255", ["255.255.255.255"]),
        ("127.0.0.1", ["127.0.0.1"]),
        ("999.999.999.999", ["999.999.999.999"]),  # Invalid IP but matches pattern
        ("192.168.1.1:8080", ["192.168.1.1"]),  # Port ignored
        ("192.168.1", []),  # Incomplete IP
    ],
)
def test_Extract_IPv4(text, expected):
    logger.debug(f"Testing Extract_IPv4 with input: {text}")
    result = Extract_IPv4(text)
    assert sorted(result) == sorted(expected)

# Tests for Extract_UUIDs
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # ✅ Valid UUIDs (lowercase, uppercase, mixed-case)
        ("UUID: 123e4567-e89b-12d3-a456-426614174000",
         ["123e4567-e89b-12d3-a456-426614174000"]),

        ("Uppercase UUID: 123E4567-E89B-12D3-A456-426614174000",
         ["123e4567-e89b-12d3-a456-426614174000"]),

        ("Mixed-case UUID: 123e4567-E89B-12d3-a456-426614174000",
         ["123e4567-e89b-12d3-a456-426614174000"]),

        # ✅ Multiple UUIDs separated by punctuation
        ("UUIDs: 123e4567-e89b-12d3-a456-426614174000, a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11!",
         ["123e4567-e89b-12d3-a456-426614174000", "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),

        # ✅ UUID at the start and end
        ("123e4567-e89b-12d3-a456-426614174000 is at the start",
         ["123e4567-e89b-12d3-a456-426614174000"]),

        ("Ends with UUID a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
         ["a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"]),

        # ✅ Edge cases
        ("No UUIDs here", []),
        ("", []),

        # ✅ Stress test: multiple UUIDs in a long string
        ("Log IDs: 123e4567-e89b-12d3-a456-426614174000  "
         "and a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11  "
         "plus 550e8400-e29b-41d4-a716-446655440000",
         [
             "123e4567-e89b-12d3-a456-426614174000",
             "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
             "550e8400-e29b-41d4-a716-446655440000",
         ]),
    ],
)
def test_Extract_UUIDs(text, expected):
    logger.debug(f"Testing Extract_UUIDs with input: {text}")
    result = Extract_UUIDs(text)
    assert sorted(result) == sorted(expected)