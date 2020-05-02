from pyavro import Schema, Field
import unittest


class TestSchema(unittest.TestCase):
    def test_schema_suceeds(self):
        schema = Schema(
            type="record",
            namespace="tests",
            name="test_schema",
            fields=[
                Field(name="message", type=str),
                Field(name="id", type=int),
                Field(name="id", type=bytes)
            ]
        )
        parsed_schema = schema.parse()
        assert isinstance(parsed_schema, dict)
        assert len(parsed_schema["fields"]) == 3
