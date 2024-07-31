import pytest
from gendiff.scripts.gendiff import generate_diff

JSON1 = "tests/fixtures/json1.json"
JSON2 = "tests/fixtures/json2.json"
YML1 = "tests/fixtures/yml1.yml"
YML2 = "tests/fixtures/yml2.yml"
STYLISH_RESULT = "tests/fixtures/stylish.txt"
PLAIN_RESULT = "tests/fixtures/plain_diff.txt"
YAML_RESULT = "tests/fixtures/json.json"


@pytest.mark.parametrize(
    "file1, file2, format_name, result_file",
    [
        (JSON1, JSON2, "stylish", STYLISH_RESULT),
        (JSON1, JSON2, "plain", PLAIN_RESULT),
        (JSON1, JSON2, "json", YAML_RESULT),
        (YML1, YML2, "stylish", STYLISH_RESULT),
        (YML1, YML2, "plain", PLAIN_RESULT),
        (YML1, YML2, "json", YAML_RESULT),
    ],
)
def test_generate_diff(file1, file2, format_name, result_file):
    with open(result_file) as f:
        expected_result = f.read().strip()
    assert generate_diff(file1, file2, format_name).strip() == expected_result
