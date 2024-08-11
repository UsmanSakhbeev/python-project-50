import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize(
    "file1, file2, format_name, result_file",
    [
        (
            "tests/fixtures/json1.json",
            "tests/fixtures/json2.json",
            "stylish",
            "tests/fixtures/stylish.txt",
        ),
        (
            "tests/fixtures/json1.json",
            "tests/fixtures/json2.json",
            "plain",
            "tests/fixtures/plain_diff.txt",
        ),
        (
            "tests/fixtures/json1.json",
            "tests/fixtures/json2.json",
            "json",
            "tests/fixtures/json.json",
        ),
        (
            "tests/fixtures/yml1.yml",
            "tests/fixtures/yml2.yml",
            "stylish",
            "tests/fixtures/stylish.txt",
        ),
        (
            "tests/fixtures/yml1.yml",
            "tests/fixtures/yml2.yml",
            "plain",
            "tests/fixtures/plain_diff.txt",
        ),
        (
            "tests/fixtures/yml1.yml",
            "tests/fixtures/yml2.yml",
            "json",
            "tests/fixtures/json.json",
        ),
    ],
)
def test_generate_diff(file1, file2, format_name, result_file):
    with open(result_file) as f:
        expected_result = f.read().strip()
    assert generate_diff(file1, file2, format_name).strip() == expected_result
