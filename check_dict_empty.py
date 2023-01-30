def empty_values(my_dict):
    """
    检查字典中值是否为空 | check if the dict value is empty
    :param my_dict: 需要检查的字典 | dict that needs to be checked
    :return empty_keys: 返回列表，包含字典中值为空的键 | return a list containing keys with empty values in the dict
            empty_values_count: 返回num，字典中值为空的键的个数 | return num, the number of keys with empty values in the dict
    """

    empty_keys = []
    empty_values_count = 0
    if all(not value for value in my_dict.values()):
        # 如果全为空，输出 All values are empty
        print("All values are empty")
    else:
        for key, value in my_dict.items():
            if not value:
                empty_keys.append(key)
                empty_values_count += 1
                # print(f"The value for key '{key}' is empty")
    return empty_keys, empty_values_count


if __name__ == "__main__":
    my_dict1 = {'a': 1, 'b': 2, 'c': None, 'd': ''}
    empty_keys1 = empty_values(my_dict1)
    print(empty_keys1)
