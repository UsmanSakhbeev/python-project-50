import pytest
from gendiff.scripts.gendiff import generate_diff


TEST_PARAMS = {
    "json_stylish": {
        "format": "stylish",
        "files_to_compare": ["tests/fixtures/json1.json",
                             "tests/fixtures/json2.json"],
        "expected_output": "tests/fixtures/stylish.txt",
    },
    "json_plain": {
        "format": "plain",
        "files_to_compare": ["tests/fixtures/json1.json",
                             "tests/fixtures/json2.json"],
        "expected_output": "tests/fixtures/plain_diff.txt",
    },
    "json_yaml": {
        "format": "json",
        "files_to_compare": ["tests/fixtures/json1.json",
                             "tests/fixtures/json2.json"],
        "expected_output": "tests/fixtures/json.json",
    },
    "yml_stylish": {
        "format": "stylish",
        "files_to_compare": ["tests/fixtures/yml1.yml",
                             "tests/fixtures/yml2.yml"],
        "expected_output": "tests/fixtures/stylish.txt",
    },
    "yml_plain": {
        "format": "plain",
        "files_to_compare": ["tests/fixtures/yml1.yml",
                             "tests/fixtures/yml2.yml"],
        "expected_output": "tests/fixtures/plain_diff.txt",
    },
    "yml_yaml": {
        "format": "json",
        "files_to_compare": ["tests/fixtures/yml1.yml",
                             "tests/fixtures/yml2.yml"],
        "expected_output": "tests/fixtures/json.json",
    },
}


@pytest.mark.parametrize("case", TEST_PARAMS.keys())
def test_generate_diff(case):
    params = TEST_PARAMS[case]
    file1, file2 = params["files_to_compare"]
    format_name = params["format"]
    with open(params["expected_output"]) as f:
        expected_result = f.read().strip()
    assert generate_diff(file1, file2, format_name).strip() == expected_result
