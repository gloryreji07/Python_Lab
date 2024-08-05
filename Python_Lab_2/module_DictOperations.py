from typing import Dict, List, Any

def merging_dicts(*args: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge multiple dictionaries into one. Later dictionaries overwrite earlier ones."""
    merged_dict = {}
    for d in args:
        merged_dict.update(d)
    return merged_dict

def common_keys(*args: Dict[Any, Any]) -> set[Any]:
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    
    common = set(args[0].keys())
    for d in args[1:]:
        common &= set(d.keys())
    return common

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """Invert a dictionary, swapping keys and values. Group keys with the same value."""
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

def common_key_value_pairs(*args: Dict[Any, Any]) -> Dict[Any, Any]:
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    
    common_pairs = set(args[0].items())
    for d in args[1:]:
        common_pairs &= set(d.items())
    
    return dict(common_pairs)
