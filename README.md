# rexa

**rexa** is a lightweight, modular Python library for advanced text processing and regular expression (regex) utilities. It empowers developers by centralizing common validation, extraction, conversion, formatting, and natural language preprocessing workflows into a clean, object‑oriented API.

---

## ✨ Features

- **Validation & Matching**: Validate emails, phone numbers, URLs, dates, UUIDs, and more with `Validator` methods (`Is_*`, `Match_*`).
- **Extraction**: Pull out emails, links, phone numbers, dates, IPs, and UUIDs from unstructured text using `Extractor`.
- **Conversion & Formatting**: Transform text formats—normalize spaces, swap date separators, remove thousand separators, generate URL slugs.
- **TextTools Utility**: Advanced text cleaning and NLP helpers in `texttools.py`:
  - Case conversion (upper/lower)
  - Emoji, punctuation, number, and mention removal
  - URL & email stripping
  - Stop‑word removal, lemmatization, stemming
  - Language detection, token counting, word‑length filtering
  - Arabic character normalization
- **Fully Tested**: 100% coverage via `pytest`, ensuring reliability.

---

## 🗂️ Installation

Install from PyPI:

```bash
pip install rexa
```

Or clone and install locally:

```bash
git clone https://github.com/arshia82sbn/rexa.git
cd rexa
pip install .
```

---

## 📦 Project Structure

```
rexa/
├── rexa/
│   ├── __init__.py
│   ├── validation.py      # Validator class: Is_*/Match_* methods
│   ├── extraction.py      # Extractor class: Extract_* methods
│   ├── conversion.py      # Converter class: Convert_* methods
│   ├── formatting.py      # Formatter class: Normalize/Strip methods
│   └── texttools.py       # TextTools class: NLP and cleaning utilities
├── tests/
│   └── test_rex.py        # pytest suite
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## 🛠️ Usage Examples

### Regex Validation & Extraction
```python
from rexa import Rex
rex = Rex()
# Validation
assert rex.Is_Email("user@example.com")
# Extraction
emails = rex.Extract_Emails("a@a.com, b@b.org")
```  

### Text Cleaning & NLP
```python
from rexa.texttools import TextTools
text = "@john Hello 😊! Visit https://example.com"
clean = TextTools.clean_text(
    text,
    lowercase=True,
    remove_emoji=True,
    remove_username=True,
    remove_urls_emails=True,
    remove_punct=True
)
print(clean)
```  

---

## ✅ Testing

Run unit tests:

```bash
pytest -q
```

---

## 🌐 Compatibility

- Python 3.10+
- Dependencies:
  - `regex`  
  - `dateparser`  
  - `pydantic >=2.0.0`  
  - `nltk`  
  - `langdetect`

---


## 🤝 Contributions

Issues, suggestions, and pull requests are welcome! Please see `CONTRIBUTING.md` for guidelines.
