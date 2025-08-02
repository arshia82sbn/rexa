"""
Entry point of the rex package. It aggregates the functionality of
validation, extraction, conversion, and formatting modules into a single importable interface.
"""

from .validation   import Validator
from .extraction   import RexExtractor
from .conversion   import RexConverter
from .formatting   import RexFormatter

# Unified class that wraps all functionalities (optional)
class Rex:
    """
    Rex: Unified interface for regex-based validation, extraction, conversion, and formatting.

    Usage:
        rex = Rex()
        rex.validator.Is_Email("test@example.com")
        rex.extractor.Extract_Emails("email1@example.com and email2@example.org")
    """

    def __init__(self):
        self.validator = Validator()
        self.extractor = RexExtractor()
        self.converter = RexConverter()
        self.formatter = RexFormatter()
