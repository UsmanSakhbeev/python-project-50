import pytest
from gendiff.scripts.gendiff import generate_diff


JSON1 = "tests/fixtures/json1.json"
JSON2 = "tests/fixtures/json2.json"
YML1 = "tests/fixtures/yml1.yml"
YML2 = "tests/fixtures/yml2.yml"
JSON_RESULT = "tests/fixtures/diff.json"
PLAIN_RESULT = "tests/fixtures/plain_diff"
YAML_RESULT = "tests/fixtures/json.json"

def test_json_merge():    

    with open(JSON_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(JSON1, JSON2, "stylish").strip() == expected_result

    with open(PLAIN_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(JSON1, JSON2, "plain").strip() == expected_result

    with open(YAML_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(JSON1, JSON2, "json").strip() == expected_result



def test_yml_merge():

    with open(JSON_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(YML1, YML2, "stylish").strip() == expected_result

    with open(PLAIN_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(YML1, YML2, "plain").strip() == expected_result

    with open(YAML_RESULT) as f:
        expected_result = f.read().strip()    
    assert generate_diff(YML1, YML2, "json").strip() == expected_result


    