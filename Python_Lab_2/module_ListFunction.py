from typing import List

def find_max(lst: List[int]) -> int:
    """Find the maximum value in a list."""
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def find_min(lst: List[int]) -> int:
    """Find the minimum value in a list."""
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def calculate_sum(lst: List[int]) -> int:
    """Calculate the sum of all elements in a list."""
    return sum(lst)

def calculate_average(lst: List[int]) -> float:
    """Compute the average of the list."""
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)

def find_median(lst: List[int]) -> float:
    """Determine the median of a list."""
    if not lst:
        raise ValueError("List is empty")
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2.0
    else:
        return sorted_lst[mid]
    
    
