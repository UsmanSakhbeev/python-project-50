import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parse_files import get_text


JSON1 = "tests/fixtures/json1.json"
JSON2 = "tests/fixtures/json2.json"
YML1 = "tests/fixtures/yml1.yml"
YML2 = "tests/fixtures/yml2.yml"
RESULT = "tests/fixtures/diff.json"

def test_json_merge():
    with open(RESULT) as f:
        expected_result = f.read().strip()
    json1, json2 = get_text(JSON1, JSON2)
    assert generate_diff(json1, json2).strip() == expected_result

def test_yml_merge():
    with open(RESULT) as f:
        expected_result = f.read().strip()
    yml1, yml2 = get_text(YML1, YML2)
    assert generate_diff(yml1, yml2).strip() == expected_result
