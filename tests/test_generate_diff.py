from gendiff.diff_with_formatter import generate_diff, stringify
import pytest


@pytest.mark.parametrize(
    'first_file, second_file, expected',
    [
        pytest.param(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json',
            'tests/fixtures/result_flat_json.txt',
            id="flat_json_file"
        ),
    ],
)
def test_generate_diff_flat_json(first_file, second_file, expected):
    with open(expected, 'r') as file:
        result_data = file.read()
    assert generate_diff(first_file, second_file) == result_data
