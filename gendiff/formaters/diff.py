def stringify(value, replacer=' ', space_count=2, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer * space_count * _lvl}{el}: '
            result += stringify(val, replacer, space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}\n'
    else:
        result = str(value)
    return result


def get_parsed_data(file1, file2):
    output_dictionary = dict()
    chaning_keys_and_values_file1 = {v: k for k, v in file1.items()}
    sorted_dictionary_file1 = sorted(chaning_keys_and_values_file1.items(), key=lambda x: x[1])
    appeal_dictionary_file1 = dict(sorted_dictionary_file1)
    new_open_file1 = {v: k for k, v in appeal_dictionary_file1.items()}
    сhanging_keys_and_values_file2 = {v: k for k, v in file2.items()}
    sorted_dictionary_file2 = sorted(сhanging_keys_and_values_file2.items(), key=lambda x: x[1])
    appeal_dictionary_file2 = dict(sorted_dictionary_file2)
    new_open_file2 = {v: k for k, v in appeal_dictionary_file2.items()}
    for keys_one in new_open_file1.keys():
        check_tmp = 0
        for keys_two in new_open_file2.keys():
            if keys_one == keys_two:
                check_tmp = 1
                if new_open_file1[keys_one] == new_open_file2[keys_two]:
                    output_dictionary['  ' + keys_one] = new_open_file1[keys_one]
                    new_open_file2.pop(keys_two)
                    break
                else:
                    output_dictionary['- ' + keys_one] = new_open_file1[keys_one]
                    output_dictionary["+ " + keys_one] = new_open_file2[keys_one]
                    new_open_file2.pop(keys_two)
                    break
        if check_tmp == 0:
            output_dictionary["- " + keys_one] = new_open_file1[keys_one]
    for keys_one in new_open_file2.keys():
        output_dictionary["+ " + keys_one] = new_open_file2[keys_one]
    dictionary_output_to_a_string = stringify(output_dictionary)
    replacing_the_value_True = dictionary_output_to_a_string.replace("True", "true")
    replacing_the_value_False = replacing_the_value_True.replace("False", "false")
    return replacing_the_value_False
