from gendiff.get_data_from_file import parse
from gendiff.formaters import formatters
from gendiff.dict_build import diff_builder


def get_content(path):
    with open(path, 'r') as file_content:
        return parse(file_content.read(), path.split('.')[-1])



def generate_diff(path_to_file1, path_to_file2, format='stylish'):
    content1 = get_content(path_to_file1)
    content2 = get_content(path_to_file2)
    diff_dict = diff_builder(content1, content2)
    return formatters(format, diff_dict)

def prom(ls1,ls2):
    ls1,ls2 = ls1[::-1],ls2[::-2]
    po = str(ls1)
    p = ''.join(po)
    return p


l1 = [2,4,3]
l2 = [5,6,4]
print(prom(l1,l2))