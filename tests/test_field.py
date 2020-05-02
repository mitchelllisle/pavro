from pyavro import Field
import unittest


class TestField(unittest.TestCase):
    def test_field_success(self):
        int_field = Field(name="id", type=int)
        pass
