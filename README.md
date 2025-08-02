# rexa

**rexa** is a lightweight and modular Python library for regular expression (regex) utilities, offering easy-to-use tools for validation, extraction, conversion, and formatting. Designed for developers who need powerful yet readable regex functionalities, `rexa` keeps your code clean and your logic centralized.

---

## ✨ Features

- Validate common patterns: email, phone number, IP address, date, etc.
- Extract specific data from unstructured text.
- Convert between different formats (dates, numbers, text).
- Format and normalize messy strings.
- Fully modular and extensible design.
- Written in modern Python with object-oriented architecture.
- Fully tested with `pytest`.

---

## 🚀 Quick Start

### Installation

```
pip install rexa
```

> Alternatively, if you're cloning manually:

```
git clone https://github.com/your-username/rexa.git
cd rexa
pip install .
```

---

## 📚 Usage

```python
from rexa import Rex

rex = Rex()

# Validation
rex.Is_Email("user@example.com")           # True
rex.Is_Date("2025-08-02")                  # True

# Extraction
rex.Extract_Emails("Contact: a@b.com, c@d.com")
# ['a@b.com', 'c@d.com']

# Conversion
rex.Convert_DateFormat("02.08.2025", from_sep=".", to_sep="/")
# '02/08/2025'

# Formatting
rex.Slugify("Hello, World!")
# 'hello-world'
```

---

## 🗂️ Modules

- `validation.py`: Input pattern validation functions
- `extraction.py`: Email, phone, and pattern extraction
- `conversion.py`: Format transformations for text and numbers
- `formatting.py`: Text normalization and cleanup

---

## ✅ Tests

All functions are fully tested with `pytest`. To run tests:

```bash
pytest -q
```

---

## 🌐 Compatibility

- Python 3.7+
- No external dependencies (only standard library and `re` module)

---

## 🛍️ Feedback & Contributions

Issues, suggestions, and pull requests are welcome!

Start using `rexa` today to supercharge your regex workflows with elegant and maintainable Python code.

