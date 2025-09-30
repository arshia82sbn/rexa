🎉 Rexa Usage Guide
Welcome to Rexa, a powerful Python library for regex operations and text preprocessing! Whether you're validating emails, extracting URLs, generating fuzzy regex patterns, or cleaning text for NLP pipelines, Rexa has you covered. This guide provides clear examples to help you harness Rexa's full potential.

🚀 Getting Started
Install Rexa via pip:
pip install rexa

Import and use:
from rexa import Rex
rex = Rex()

# Example: Validate an email
print(rex.validator.Is_Email("user@example.com"))  # True

# Example: Generate fuzzy regex
print(rex.mapper.string_to_regex("i'm"))  # \b[iIíìîïİ1!|]['‘’][mM]\b

Dependencies: Requires Python 3.10+, regex, dateparser, pydantic, nltk, langdetect.
Source: GitHub | Issues

🔍 1. Validator (validation.py)
Validate and match common patterns with ease:



Method
Description
Example



Is_Email(s)
✅ Checks if s is a valid email
rex.validator.Is_Email("user@example.com") → True


Match_Email(s)
🔎 Returns Match object for email, else None
rex.validator.Match_Email("bad@") → None


Is_URL(s)
✅ Validates HTTP/HTTPS URLs
rex.validator.Is_URL("https://site.io") → True


Match_URL(s)
🔎 Matches URL and captures path/query
m = rex.validator.Match_URL("site.com/path")


Is_Date_ISO(s)
✅ Checks YYYY-MM-DD date format
rex.validator.Is_Date_ISO("2025-08-02") → True


Match_Date_ISO(s)
🔎 Captures ISO date, if present
rex.validator.Match_Date_ISO("02/08/2025") → None


Is_IranianPhone(s)
✅ Validates Iranian mobile numbers
rex.validator.Is_IranianPhone("09121234567") → True


Is_UUID4(s)
✅ Checks UUID v4 format
rex.validator.Is_UUID4("123e4567-e89b-12d3-a456-426614174000") → True


And more
Methods for time, ISBN, hex colors, etc.
See validation.py for full list



📥 2. Extractor (extraction.py)
Extract specific patterns from text:



Method
Extracts…
Example



Extract_Emails(text)
All email addresses
rex.extractor.Extract_Emails("a@a.com b@b.org") → ["a@a.com", "b@b.org"]


Extract_URLs(text)
All web links (http/https/ftp)
rex.extractor.Extract_URLs("Go to http://x.com") → ["http://x.com"]


Extract_Dates(text)
Dates in ISO/EU formats
rex.extractor.Extract_Dates("2021-01-01 or 01/01/2021") → ["2021-01-01", "01/01/2021"]


Extract_Phones(text)
Phone numbers (intl & local)
rex.extractor.Extract_Phones("+123456789, 09121234567") → ["+123456789", "09121234567"]


Extract_IPv4(text)
IPv4 addresses
rex.extractor.Extract_IPv4("192.168.1.1") → ["192.168.1.1"]


Extract_UUIDs(text)
UUID v4 strings
rex.extractor.Extract_UUIDs("123e4567-e89b-12d3-a456-426614174000") → ["123e4567-e89b-12d3-a456-426614174000"]



🔄 3. Converter (conversion.py)
Normalize and reformat strings:



Method
Description
Example



Convert_MultipleSpaces(text)
Collapses extra spaces
rex.converter.Convert_MultipleSpaces("A   B") → "A B"


Convert_ThousandSeparatedNumbers(text)
Strips commas from large numbers
rex.converter.Convert_ThousandSeparatedNumbers("1,000,000") → "1000000"


Convert_DateFormat(s, from, to)
Swaps date separators
rex.converter.Convert_DateFormat("01.01.2025", ".", "/") → "01/01/2025"


Slugify(text)
Generates SEO-friendly URL slugs
rex.converter.Slugify("Hello World!") → "hello-world"



✨ 4. Formatter (formatting.py)
Clean and standardize text:



Method
Description
Example



Strip_HTMLTags(s)
Removes HTML tags
rex.formatter.Strip_HTMLTags("<b>Hi</b>") → "Hi"


Normalize_Spaces(s)
Normalizes to single spaces
rex.formatter.Normalize_Spaces("A   B") → "A B"


Remove_ThousandSeparators(s)
Drops commas in numbers
rex.formatter.Remove_ThousandSeparators("1,234") → "1234"


Normalize_DateSeparator(s, sep)
Standardizes date delimiters
rex.formatter.Normalize_DateSeparator("2021/01.01", "-") → "2021-01-01"



🧠 5. Regex Mapper (regex_mapper.py)
Generate fuzzy regex patterns and analyze text structure:



Method
Description
Example



string_to_regex(text, use_anchors=False, use_char_map=True, detailed=False)
Generates a fuzzy regex pattern for text. Use use_anchors=True for ^...$, use_char_map=True for fuzzy matching (e.g., i → `[iIíìîïİ1!
]), detailed=True` for validation info.


string_to_breakdown(text, use_char_map=True, detailed=False)
Breaks down text into regex components with metadata (type, pattern, count). detailed=True adds Unicode categories and variant matches.
rex.mapper.string_to_breakdown("i'm") → `[{"type": "LETTER", "name": "fuzzy 'i'", "pattern": "[iIíìîïİ1!


get_all_patterns()
Returns a dictionary of predefined patterns (email, URL, etc.)
rex.mapper.get_all_patterns() → {"email": "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", ...}


Example with Detailed Output:
# Detailed regex
pattern, details = rex.mapper.string_to_regex("i'm", detailed=True)
print(pattern)  # \b[iIíìîïİ1!|]['‘’][mM]\b
print(details)  # {'valid': True, 'score': 0.75, 'sample_matches': ["i'm", "I'm", "1'm"], 'explanation': 'Pattern matches original: True...'}

# Detailed breakdown
breakdown = rex.mapper.string_to_breakdown("i'm", detailed=True)
print(breakdown[0])  # {'type': 'LETTER', 'name': "fuzzy 'i'", 'pattern': '[iIíìîïİ1!|]', 'count': 1, 'example_chars': ['i'], 'unicode_category': 'Ll', 'variant_matches': ['i', 'I', '1']}


🧹 6. TextTools (texttools.py)
Advanced NLP and text cleaning utilities:



Method
Description
Example



to_lower(s)
Lowercases entire string
rex.texttools.to_lower("HELLO") → "hello"


to_upper(s)
Uppercases entire string
rex.texttools.to_upper("hi") → "HI"


remove_emojis(s)
Strips Unicode emojis
rex.texttools.remove_emojis("I ❤️ you") → "I  you"


remove_numbers(s)
Removes all digits
rex.texttools.remove_numbers("a1b2") → "ab"


remove_usernames(s)
Removes @username tokens
rex.texttools.remove_usernames("@me hi") → " hi"


remove_punctuation(s)
Strips punctuation & symbols
rex.texttools.remove_punctuation("Hey!?@") → "Hey"


remove_urls_emails(s)
Drops URLs & email addresses
rex.texttools.remove_urls_emails("a@b.com http://x") → " "


remove_stopwords(s)
Filters common words (using NLTK)
rex.texttools.remove_stopwords("the cat sits") → "cat sits"


lemmatize_text(s)
Lemmatizes tokens
rex.texttools.lemmatize_text("running") → "running"


stem_text(s)
Stems tokens
rex.texttools.stem_text("running") → "run"


normalize_whitespace(s)
Collapses whitespace
rex.texttools.normalize_whitespace(" A  B\n") → "A B"


normalize_arabic(s)
Persian/Arabic char mapping & diacritics
rex.texttools.normalize_arabic("كیف") → "کیف"


count_tokens(s)
Counts word tokens
rex.texttools.count_tokens("a b c") → 3


remove_short_long_words(s, min, max)
Keeps words in length range
rex.texttools.remove_short_long_words("a bb ccc", 2, 3) → "bb ccc"


detect_language(s)
Auto-detects text language
rex.texttools.detect_language("hello") → "en"


clean_text(...kwargs)
Pipeline for common cleaning options
rex.texttools.clean_text("Hi @you 123 😊", lowercase=True, remove_emoji=True, remove_username=True, remove_urls_emails=True, remove_punct=True) → "hi"



🚀 Quick Tips

Mix & Match: Combine methods for complex workflows, e.g., rex.texttools.clean_text() followed by rex.extractor.Extract_Emails().
Fuzzy Matching: Use string_to_regex with use_char_map=True for robust pattern generation (e.g., matches i'm, I'm, 1'm).
Performance: For large texts, batch process with map() or parallelize with multiprocessing.
Extensibility: Subclass Rex to add custom patterns or preprocessing steps.
Debugging: Enable logging (via utils.Logger) for detailed insights into regex generation and validation.


📚 Example Workflow
Clean and validate user input:
from rexa import Rex
rex = Rex()

text = "Contact: alice@example.com, bob@TEST.org   Date: 2025-08-02 😊"
cleaned = rex.texttools.clean_text(text, lowercase=True, remove_emoji=True)
emails = rex.extractor.Extract_Emails(cleaned)
is_valid_date = rex.validator.Is_Date_ISO("2025-08-02")
pattern = rex.mapper.string_to_regex("alice", use_char_map=True)
print(cleaned)  # contact: alice@example.com, bob@test.org date: 2025-08-02
print(emails)   # ['alice@example.com', 'bob@test.org']
print(is_valid_date)  # True
print(pattern)  # \b[aAáàâäãåā@4][lL1|][iIíìîïİ1!|][cCçćč][eEéèêëē3]\b


Happy coding with Rexa! Questions or feedback? Open an issue at https://github.com/arshia82sbn/rexa/issues.