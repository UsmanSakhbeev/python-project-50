import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.parse_files import get_text


JSON1 = "tests/fixtures/json1.json"
JSON2 = "tests/fixtures/json2.json"
YML1 = "tests/fixtures/yml1.yml"
YML2 = "tests/fixtures/yml2.yml"
JSON_RESULT = "tests/fixtures/diff.json"
PLAIN_RESULT = "tests/fixtures/plain_diff"

def test_json_merge():
    json1, json2 = get_text(JSON1, JSON2)

    with open(JSON_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(json1, json2, "stylish").strip() == expected_result

    with open(PLAIN_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(json1, json2, "plain").strip() == expected_result



def test_yml_merge():
    yml1, yml2 = get_text(YML1, YML2)

    with open(JSON_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(yml1, yml2, "stylish").strip() == expected_result

    with open(PLAIN_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(yml1, yml2, "plain").strip() == expected_result
