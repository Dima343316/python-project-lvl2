from gendiff.diff_with_formatter import generate_diff
import pytest

@pytest.mark.parametrize(
    'first_file, second_file, expected',
    [
        pytest.param(
            'fixtures/file1.json',
            'fixtures/file2.json',
            'fixtures/result_flat_json.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'fixtures/file1.yml',
            'fixtures/file2.yml',
            'fixtures/result_flat_json.txt',
            id="flat_yml_file"
        ),
    ],
)


def test_generate_diff_flat_json(first_file, second_file, expected):
    with open(expected, 'r') as file:
        result_data = file.read()
    assert generate_diff(first_file, second_file) == result_data


@pytest.mark.parametrize(
    'file1, file2, result',
    [
        pytest.param(
            'fixtures/file3.json',
            'fixtures/file4.json',
            'fixtures/result_nested_json.txt',
            id="flat_json_file"
        ),
    ],
)



def test_generate_nested_json(file1, file2, result):
    with open(result, 'r') as file:
        result_data = file.read()
    assert generate_diff(file1, file2) == result_data


@pytest.mark.parametrize(
    'file3, file4, result_yml',
    [
        pytest.param(
            'fixtures/file3.yml',
            'fixtures/file4.yml',
            'fixtures/result_nested_json.txt',
            id="nested_yml_file"
        ),
    ],
)


def test_generate_nested_yml(file3,file4,result_yml):
    with open(result_yml, 'r') as file:
        result_data = file.read()
    assert generate_diff(file3, file4) == result_data


@pytest.mark.parametrize(
    'file3, file4, result_json_plain',
    [
        pytest.param(
            'fixtures/file3.json',
            'fixtures/file4.json',
            'fixtures/result_nested_plain.txt',
            id="nested_json_file_plain"
        ),
    ],
)

def test_generate_nested_plain(file3,file4, result_json_plain):
    with open(result_json_plain, 'r') as file:
        result_date = file.read()
    assert generate_diff(file3,file4,format='plain') == result_date

@pytest.mark.parametrize(
     'file3, file4',
     [
        pytest.param(
            'fixtures/file3.json',
            'fixtures/file4.json',
            id="nested_json_file_plain"
        ),
    ],
)

def test_generate_error_format(file3,file4):

    with pytest.raises(Exception):
        generate_diff(file3,file4,format='plain')


@pytest.mark.parametrize(
     'file3, file4',
     [
        pytest.param(
            'fixtures/file3.json',
            'fixtures/file4.json',
            id="nested_json_file_plain"
        ),
    ],
)

def test_generate_error_format_stylish(file3,file4):
    with pytest.raises(Exception):
        generate_diff(file3,file4,format='stylish')

@pytest.mark.parametrize(
    'file3, file4, result_nested_json_format',
    [
        pytest.param(
            'fixtures/file3.json',
            'fixtures/file4.json',
            'fixtures/result_nested_json_format.txt',
            id="nested_json_file_plain"
        ),
    ],
)

def test_generate_nested_plain(file3,file4, result_nested_json_format):
    with open(result_nested_json_format, 'r') as file:
        result_date = file.read()
    assert generate_diff(file3,file4,format='json') == result_date