from typing import Set, List, FrozenSet

def add_element(s: Set, element) -> None:
    """Add an element to a set, ignoring if the element already exists."""
    s.add(element)

def remove_element(s: Set, element) -> None:
    """Remove an element from a set, ignoring if the element does not exist."""
    s.discard(element)  

def union_of_sets(s1: Set, s2: Set) -> Set:
    """Return the union of two sets."""
    return s1.union(s2)

def intersection_of_sets(s1: Set, s2: Set) -> Set:
    """Return the intersection of two sets."""
    return s1.intersection(s2)

def difference_of_sets(s1: Set, s2: Set) -> Set:
    """Return the difference S1 - S2."""
    return s1.difference(s2)

def is_subset(s1: Set, s2: Set) -> bool:
    """Check if set S1 is a subset of set S2."""
    return s1.issubset(s2)

def length_of_set(s: Set) -> int:
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference_of_sets(s1: Set, s2: Set) -> Set:
    """Compute the symmetric difference of two sets."""
    return s1.symmetric_difference(s2)

def power_set(s: Set) -> Set[FrozenSet]:
    """Compute the power set of a given set."""
    power_set_list = []
    set_list = list(s)
    for i in range(2 ** len(set_list)):
        subset = frozenset(set_list[j] for j in range(len(set_list)) if (i >> j) & 1)
        power_set_list.append(subset)
    return set(power_set_list)

def unique_subsets(s: Set) -> Set[FrozenSet]:
    """Get all unique subsets of a given set."""
    return power_set(s)
