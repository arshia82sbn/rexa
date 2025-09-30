import re
import nltk
import unicodedata
from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Ensure necessary NLTK resources are available
nltk.download('stopwords',quiet=True)
nltk.download('punkt',quiet=True)
nltk.download('wordnet',quiet=True)
"""
A collection of static methods for text preprocessing and normalization.
"""

def to_lower(text: str) -> str:
    return text.lower()

def to_upper(text: str) -> str:
    return text.upper()

def remove_emojis(text: str) -> str:
    return ''.join(c for c in text if not unicodedata.category(c).startswith('So'))

def remove_numbers(text: str) -> str:
    return re.sub(r'\d+', '', text)

def remove_usernames(text: str) -> str:
    return re.sub(r'@\w+', '', text)

def remove_punctuation(text: str) -> str:
    return re.sub(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~؟،٫؛]', '', text)

def remove_stopwords(text: str, language='english') -> str:
    words = nltk.word_tokenize(text)
    stop_words = set(stopwords.words(language))
    filtered = [w for w in words if w.lower() not in stop_words]
    return ' '.join(filtered)

def lemmatize_text(text: str) -> str:
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(text)
    lemmatized = [lemmatizer.lemmatize(w) for w in words]
    return ' '.join(lemmatized)

def stem_text(text: str) -> str:
    stemmer = PorterStemmer()
    words = nltk.word_tokenize(text)
    stemmed = [stemmer.stem(w) for w in words]
    return ' '.join(stemmed)

def remove_urls_emails(text: str) -> str:
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    return text

def normalize_whitespace(text: str) -> str:
    return ' '.join(text.split())

def normalize_arabic(text: str) -> str:
    arabic_map = {
        'ك': 'ک',
        'ي': 'ی',
        'ة': 'ه',
        '‌': '',  # ZWNJ
        'َ': '', 'ً': '', 'ُ': '', 'ٌ': '', 'ِ': '', 'ٍ': '', 'ْ': '', 'ّ': ''
    }
    for key, val in arabic_map.items():
        text = text.replace(key, val)
    return text

def count_tokens(text: str) -> int:
    return len(nltk.word_tokenize(text))

def remove_short_long_words(text: str, min_len=1, max_len=100) -> str:
    words = nltk.word_tokenize(text)
    filtered = [w for w in words if min_len <= len(w) <= max_len]
    return ' '.join(filtered)

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "unknown"

def clean_text(text, lowercase=False, remove_emoji=False, remove_number=False, remove_username=False, remove_urls_emails=False, remove_punct=False):
    result = text
    if lowercase:
        result = result.lower()
    if remove_emoji:
        result = ''.join(c for c in result if not (0x1F600 <= ord(c) <= 0x1F64F))
    if remove_number:
        result = ''.join(c for c in result if not c.isdigit())
    if remove_username:
        result = re.sub(r'@\w+', '', result)
    if remove_urls_emails:
        result = re.sub(r'\b(?:https?://|www\.)\S+\b|\b\S+@\S+\.\S+\b', '', result)
    if remove_punct:
        result = ''.join(c for c in result if c not in string.punctuation)
    return result.strip()
