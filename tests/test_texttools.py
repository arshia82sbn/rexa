# tests/test_texttools.py

import pytest
import re
from rexa.texttools import (
    to_lower,
    to_upper,
    remove_emojis,
    remove_numbers,
    remove_usernames,
    remove_punctuation,
    remove_stopwords,
    lemmatize_text,
    stem_text,
    remove_urls_emails,
    normalize_whitespace,
    normalize_arabic,
    count_tokens,
    remove_short_long_words,
    detect_language,
    clean_text
)
from utils.Logger import get_logger

logger = get_logger()

# Tests for to_lower
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("HELLO", "hello"),
        ("Mixed Case", "mixed case"),
        ("", ""),
        ("123", "123"),
        ("Hello World!", "hello world!"),
    ],
)
def test_to_lower(text, expected):
    logger.debug(f"Testing to_lower with input: {text}")
    assert to_lower(text) == expected

# Tests for to_upper
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello", "HELLO"),
        ("Mixed Case", "MIXED CASE"),
        ("", ""),
        ("123", "123"),
        ("Hello World!", "HELLO WORLD!"),
    ],
)
def test_to_upper(text, expected):
    logger.debug(f"Testing to_upper with input: {text}")
    assert to_upper(text) == expected

# Tests for remove_emojis
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello 😊 World", "Hello  World"),
        ("No emojis", "No emojis"),
        ("", ""),
        ("😊😊", ""),
        ("Emoji at end 😊", "Emoji at end "),
    ],
)
def test_remove_emojis(text, expected):
    logger.debug(f"Testing remove_emojis with input: {text}")
    assert remove_emojis(text) == expected

# Tests for remove_numbers
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("123abc456", "abc"),
        ("No numbers", "No numbers"),
        ("", ""),
        ("1 2 3", "  "),
        ("Numbers 123 end", "Numbers  end"),
    ],
)
def test_remove_numbers(text, expected):
    logger.debug(f"Testing remove_numbers with input: {text}")
    assert remove_numbers(text) == expected

# Tests for remove_usernames
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello @user world", "Hello  world"),
        ("No @usernames", "No "),
        ("", ""),
        ("@user1 @user2", " "),
        ("@user at end", " at end"),
    ],
)
def test_remove_usernames(text, expected):
    logger.debug(f"Testing remove_usernames with input: {text}")
    assert remove_usernames(text) == expected

# Tests for remove_punctuation
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello! World.", "Hello World"),
        ("No punctuation", "No punctuation"),
        ("", ""),
        ("?!@#", ""),
        ("Punct in middle! end", "Punct in middle end"),
    ],
)
def test_remove_punctuation(text, expected):
    logger.debug(f"Testing remove_punctuation with input: {text}")
    assert remove_punctuation(text) == expected

# Tests for remove_stopwords
@pytest.mark.parametrize(
    ("text", "language", "expected"),
    [
        ("The quick brown fox jumps over the lazy dog", "english", "quick brown fox jumps lazy dog"),
        ("No stop words", "english", "stop words"),
        ("", "english", ""),
        ("Le chat et le chien", "french", "chat chien"),
    ],
)
def test_remove_stopwords(text, language, expected):
    logger.debug(f"Testing remove_stopwords with input: {text}")
    assert remove_stopwords(text, language) == expected

# Tests for lemmatize_text
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("running runs ran", "running run ran"),
        ("No lemmatization", "No lemmatization"),
        ("", ""),
        ("cats cat", "cat cat"),
    ],
)
def test_lemmatize_text(text, expected):
    logger.debug(f"Testing lemmatize_text with input: {text}")
    assert lemmatize_text(text) == expected

# Tests for stem_text
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("running runs ran", "run run ran"),
        ("No stemming", "no stem"),
        ("", ""),
        ("cats cat", "cat cat"),
    ],
)
def test_stem_text(text, expected):
    logger.debug(f"Testing stem_text with input: {text}")
    assert stem_text(text) == expected

# Tests for remove_urls_emails
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("http://example.com email@example.com text", "  text"),
        ("No URLs or emails", "No URLs or emails"),
        ("", ""),
        ("https://x.com email@domain.com", " "),
    ],
)
def test_remove_urls_emails(text, expected):
    logger.debug(f"Testing remove_urls_emails with input: {text}")
    assert remove_urls_emails(text) == expected

# Tests for normalize_whitespace
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("A   B\tC\nD", "A B C D"),
        (" No extra spaces ", "No extra spaces"),
        ("", ""),
        ("  Multiple   spaces  ", "Multiple spaces"),
    ],
)
def test_normalize_whitespace(text, expected):
    logger.debug(f"Testing normalize_whitespace with input: {text}")
    assert normalize_whitespace(text) == expected

# Tests for normalize_arabic
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("كيبورد", "کیبورد"),
        ("No Arabic", "No Arabic"),
        ("", ""),
        ("ةي", "هی"),
    ],
)
def test_normalize_arabic(text, expected):
    logger.debug(f"Testing normalize_arabic with input: {text}")
    assert normalize_arabic(text) == expected

# Tests for count_tokens
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello world", 2),
        ("single", 1),
        ("", 0),
        ("word1 word2 word3", 3),
    ],
)
def test_count_tokens(text, expected):
    logger.debug(f"Testing count_tokens with input: {text}")
    assert count_tokens(text) == expected

# Tests for remove_short_long_words
@pytest.mark.parametrize(
    ("text", "min_len", "max_len", "expected"),
    [
        ("a bb ccc dddd", 2, 3, "bb ccc"),
        ("all good", 1, 100, "all good"),
        ("", 1, 100, ""),
        ("short longword", 3, 5, "short"),
    ],
)
def test_remove_short_long_words(text, min_len, max_len, expected):
    logger.debug(f"Testing remove_short_long_words with input: {text}")
    assert remove_short_long_words(text, min_len, max_len) == expected

# Tests for detect_language
@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("check", "de"),
        ("salut", "fi"),
        ("", "unknown"),
        ("hola", "cy"),
    ],
)
def test_detect_language(text, expected):
    logger.debug(f"Testing detect_language with input: {text}")
    assert detect_language(text) == expected

# Tests for clean_text
@pytest.mark.parametrize(
    ("text", "kwargs", "expected"),
    [
        ("Hello World!", {"lowercase": True}, "hello world!"),
        ("Hello @user 😊 123!", {"lowercase": True, "remove_emoji": True, "remove_number": True, "remove_username": True, "remove_punct": True}, "hello"),
        ("", {}, ""),
        ("Punct! Test.", {"remove_punct": True}, "Punct Test"),
    ],
)
def test_clean_text(text, kwargs, expected):
    logger.debug(f"Testing clean_text with input: {text}")
    assert clean_text(text, **kwargs) == expected