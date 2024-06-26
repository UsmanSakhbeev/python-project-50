import pytest
from gendiff.scripts.gendiff import generate_diff


JSON1 = "tests/fixtures/json1.json"
JSON2 = "tests/fixtures/json2.json"
JSON_RESULT = "tests/fixtures/diff_json.json"

def test_merge():
    assert generate_diff(JSON1, JSON2) == JSON_RESULT