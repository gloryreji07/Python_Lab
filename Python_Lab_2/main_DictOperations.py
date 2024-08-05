import module_DictOperations as mdo

def demonstrate_dict_operations():
  
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 2, 'c': 4, 'd': 5}
    dict3 = {'b': 2, 'c': 3, 'e': 6}

    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Dictionary 3:", dict3)

    merged_dict = mdo.merging_dicts(dict1, dict2, dict3)
    print("Merged Dictionary:", merged_dict)

    common_keys = mdo.common_keys(dict1, dict2, dict3)
    print("Common Keys:", common_keys)

    inverted_dict = mdo.invert_dict(dict1)
    print("Inverted Dictionary (Dict1):", inverted_dict)

    common_kv_pairs = mdo.common_key_value_pairs(dict1, dict2, dict3)
    print("Common Key-Value Pairs:", common_kv_pairs)

if __name__ == "__main__":
    demonstrate_dict_operations()
