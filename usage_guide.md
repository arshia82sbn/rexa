# 🎉 Rexa Usage Guide

Welcome to **Rexa**, your one-stop Python library for powerful regex operations and text preprocessing! Whether you’re building web scrapers, form validators, or NLP pipelines, this guide will help you harness Rexa’s full potential.

---

## 🔍 1. Validator (`validation.py`)
Validate and match common patterns with ease:

| Method                      | What it does                                          | Example                                                |
|-----------------------------|-------------------------------------------------------|--------------------------------------------------------|
| `Is_Email(s)`               | ✅ Returns True if `s` is a valid email               | `Rex().Is_Email("user@example.com")  # True`         |
| `Match_Email(s)`            | 🔎 Returns a Match object for valid email, else None  | `Rex().Match_Email("bad@")  # None`                   |
| `Is_URL(s)`                 | ✅ Validate HTTP/HTTPS URLs                           | `Rex().Is_URL("https://site.io")  # True`             |
| `Match_URL(s)`              | 🔎 Match URL and capture path/query                   | `m = Rex().Match_URL("site.com/path")`                |
| `Is_Date_ISO(s)`            | ✅ Check `YYYY-MM-DD` date format                      | `Rex().Is_Date_ISO("2025-08-02")  # True`             |
| `Match_Date_ISO(s)`         | 🔎 Capture ISO date, if present                       | `Rex().Match_Date_ISO("02/08/2025")  # None`          |

*And many more `Is_*` / `Match_*` methods for phones, UUIDs, etc.*

---

## 📥 2. Extractor (`extraction.py`)
Pull data out of messy text:

| Method                          | Extracts…                                | Example                                                      |
|---------------------------------|------------------------------------------|--------------------------------------------------------------|
| `Extract_Emails(text)`          | All email addresses                      | `Rex().Extract_Emails("a@a.com b@b.org")` # [`a@a.com`,`b@b.org`] |
| `Extract_URLs(text)`            | All web links                            | `Rex().Extract_URLs("Go to http://x.com")` # [`http://x.com`]    |
| `Extract_Dates(text)`           | Dates in ISO/EU formats                  | `Rex().Extract_Dates("2021-01-01 or 01/01/2021")`           |
| `Extract_Phones(text)`          | Phone numbers (intl & local)             | `Rex().Extract_Phones("+123456789, 09121234567")`           |

*…plus IPv4, UUIDs, and more.*

---

## 🔄 3. Converter (`conversion.py`)
Normalize and reformat strings:

| Method                                  | Transforms…                                   | Example                                                      |
|-----------------------------------------|-----------------------------------------------|--------------------------------------------------------------|
| `Convert_MultipleSpaces(text)`          | Collapse extra spaces                         | `Rex().Convert_MultipleSpaces("A   B")` → `"A B"`        |
| `Convert_ThousandSeparatedNumbers(text)`| Strip commas from large numbers               | `Rex().Convert_ThousandSeparatedNumbers("1,000,000")` → `"1000000"` |
| `Convert_DateFormat(s,from,to)`         | Swap date separators                          | `Rex().Convert_DateFormat("01.01.2025",".","/")` → `"01/01/2025"` |
| `Slugify(text)`                         | Generate SEO-friendly URL slugs               | `Rex().Slugify("Hello World!")` → `"hello-world"`         |

---

## ✨ 4. Formatter (`formatting.py`)
Clean up and standardize:

| Method                           | Cleans…                          | Example                                            |
|----------------------------------|----------------------------------|----------------------------------------------------|
| `Strip_HTMLTags(s)`              | Remove HTML tags                 | `Rex().Strip_HTMLTags("<b>Hi</b>")` → `"Hi"`     |
| `Normalize_Spaces(s)`            | Single-space normalization       | `Rex().Normalize_Spaces("A   B")` → `"A B"`     |
| `Remove_ThousandSeparators(s)`   | Drop commas in numbers           | `Rex().Remove_ThousandSeparators("1,234")` → `"1234"` |
| `Normalize_DateSeparator(s,sep)` | Consistent date delimiter        | `Rex().Normalize_DateSeparator("2021/01.01","-")` → `"2021-01-01"` |

---

## 🧹 5. TextTools (`texttools.py`)
Advanced NLP & text cleaning utilities:

| Method                               | Description                              | Example                                                       |
|--------------------------------------|------------------------------------------|---------------------------------------------------------------|
| `to_lower(s)`                        | Lowercase entire string                  | `TextTools.to_lower("HELLO")` → `"hello"`                   |
| `to_upper(s)`                        | Uppercase entire string                  | `TextTools.to_upper("hi")` → `"HI"`                         |
| `remove_emojis(s)`                   | Strip Unicode emojis                     | `TextTools.remove_emojis("I ❤️ you")` → `"I  you"`         |
| `remove_numbers(s)`                  | Remove all digits                        | `TextTools.remove_numbers("a1b2")` → `"ab"`                |
| `remove_usernames(s)`                | Remove `@username` tokens                | `TextTools.remove_usernames("@me hi")` → `" hi"`            |
| `remove_punctuation(s)`              | Strip punctuation & symbols              | `TextTools.remove_punctuation("Hey!?@")` → `"Hey"`         |
| `remove_urls_emails(s)`              | Drop URLs & email addresses              | `TextTools.remove_urls_emails("a@b.com http://x")` → `" "`  |
| `remove_stopwords(s)`                | Filter common words (using NLTK)         | `TextTools.remove_stopwords("the cat sits")` → `"cat sits"`  |
| `lemmatize_text(s)`                  | Lemmatize tokens                         | `TextTools.lemmatize_text("running")` → `"running"`         |
| `stem_text(s)`                       | Stem tokens                              | `TextTools.stem_text("running")` → `"run"`                  |
| `normalize_whitespace(s)`            | Collapse whitespace                      | `TextTools.normalize_whitespace(" A  B\n")` → `"A B"`    |
| `normalize_arabic(s)`                | Persian/Arabic char mapping & diacritics | `TextTools.normalize_arabic("كیف")` → `"کیف"`              |
| `count_tokens(s)`                    | Count word tokens                        | `TextTools.count_tokens("a b c")` → `3`                       |
| `remove_short_long_words(s,min,max)` | Keep words len in range                  | `TextTools.remove_short_long_words("a bb ccc",2,3)` → `"bb ccc"` |
| `detect_language(s)`                 | Auto-detect text language                | `TextTools.detect_language("hello")` → `"en"`              |
| `clean_text(...kwargs)`             | Pipeline for common cleaning options     | `TextTools.clean_text("Hi @you 123 😊", lowercase=True, remove_emoji=True, remove_username=True, remove_urls_emails=True, remove_punct=True)` → `"hi"` |

---

## 🚀 Quick Tips

- **Mix & Match**: Call only the methods you need or use `clean_text` for a one-shot pipeline.  
- **Extendable**: Create subclasses to add domain-specific patterns.  
- **Performance**: For bulk text, parallelize tokenization and regex calls.  

Happy coding with **Rexa**! Questions or feedback? Open an issue at https://github.com/arshia82sbn/rexa/issues
