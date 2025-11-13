"""
Module for validating quotes against source texts.
Uses simple matching techniques.
"""

import re


class SimpleQuoteValidator:
    def __init__(self):
        pass

    def _exact_match(self, quote: str, source_text: str) -> bool:
        quote_clean = re.sub(r"\s+", " ", quote.strip().lower())
        source_clean = re.sub(r"\s+", " ", source_text.strip().lower())
        return True if quote_clean in source_clean else False

    def validate_quote(self, quote: str, source_text: str) -> bool:
        exact_match = self._exact_match(quote, source_text)
        return exact_match
