from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain
from gendiff.formaters.json import format_json


def formatters(format, diff_dict):
    if format == 'stylish':
        return format_stylish(diff_dict)
    elif format == 'plain':
        return format_plain(diff_dict)
    elif format == 'json':
        return format_json(diff_dict)
    else:
        raise Exception(f"Unknown formatter: {format}")
