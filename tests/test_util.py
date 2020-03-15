import pytest
import unittest
from pyavro.util import match_regex_expr_or_error


class TestUtils(unittest.TestCase):
    def test_success(self):
        val = "Aa"
        self.assertEqual(
            match_regex_expr_or_error(val, "test", "^A"),
            val
        )

    def test_fail(self):
        val = "Ba"
        with pytest.raises(ValueError):
            match_regex_expr_or_error(val, "test", "^A")
