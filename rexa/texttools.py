import re
import nltk
import unicodedata
from langdetect import detect
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Ensure necessary NLTK resources are available
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

class TextTools:
    """
    A collection of static methods for text preprocessing and normalization.
    """

    @staticmethod
    def to_lower(text: str) -> str:
        return text.lower()

    @staticmethod
    def to_upper(text: str) -> str:
        return text.upper()

    @staticmethod
    def remove_emojis(text: str) -> str:
        return ''.join(c for c in text if not unicodedata.category(c).startswith('So'))

    @staticmethod
    def remove_numbers(text: str) -> str:
        return re.sub(r'\d+', '', text)

    @staticmethod
    def remove_usernames(text: str) -> str:
        return re.sub(r'@\w+', '', text)

    @staticmethod
    def remove_punctuation(text: str) -> str:
        return re.sub(r'[!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~؟،٫؛]', '', text)

    @staticmethod
    def remove_stopwords(text: str, language='english') -> str:
        words = nltk.word_tokenize(text)
        stop_words = set(stopwords.words(language))
        filtered = [w for w in words if w.lower() not in stop_words]
        return ' '.join(filtered)

    @staticmethod
    def lemmatize_text(text: str) -> str:
        lemmatizer = WordNetLemmatizer()
        words = nltk.word_tokenize(text)
        lemmatized = [lemmatizer.lemmatize(w) for w in words]
        return ' '.join(lemmatized)

    @staticmethod
    def stem_text(text: str) -> str:
        stemmer = PorterStemmer()
        words = nltk.word_tokenize(text)
        stemmed = [stemmer.stem(w) for w in words]
        return ' '.join(stemmed)

    @staticmethod
    def remove_urls_emails(text: str) -> str:
        text = re.sub(r'http\S+|www\.\S+', '', text)
        text = re.sub(r'\S+@\S+', '', text)
        return text

    @staticmethod
    def normalize_whitespace(text: str) -> str:
        return ' '.join(text.split())

    @staticmethod
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

    @staticmethod
    def count_tokens(text: str) -> int:
        return len(nltk.word_tokenize(text))

    @staticmethod
    def remove_short_long_words(text: str, min_len=1, max_len=100) -> str:
        words = nltk.word_tokenize(text)
        filtered = [w for w in words if min_len <= len(w) <= max_len]
        return ' '.join(filtered)

    @staticmethod
    def detect_language(text: str) -> str:
        try:
            return detect(text)
        except:
            return "unknown"

    @staticmethod
    def clean_text(
        text: str,
        lowercase: bool = False,
        uppercase: bool = False,
        remove_emoji: bool = False,
        remove_number: bool = False,
        remove_username: bool = False,
        remove_punct: bool = False
    ) -> str:
        if lowercase:
            text = TextTools.to_lower(text)
        if uppercase:
            text = TextTools.to_upper(text)
        if remove_emoji:
            text = TextTools.remove_emojis(text)
        if remove_number:
            text = TextTools.remove_numbers(text)
        if remove_username:
            text = TextTools.remove_usernames(text)
        if remove_punct:
            text = TextTools.remove_punctuation(text)

        text = TextTools.normalize_whitespace(text)
        return text
