import module_SetOperations as mso

def demonstrate_set_operations():
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    set3 = {10, 20, 30}
    
    print("Set 1:", set1)
    print("Set 2:", set2)
    print("Set 3:", set3)

    mso.add_element(set1, 6)
    print("Set 1 after adding 6:", set1)
    
    mso.remove_element(set1, 2)
    print("Set 1 after removing 2:", set1)

    print("Union of Set 1 and Set 2:", mso.union_of_sets(set1, set2))

    print("Intersection of Set 1 and Set 2:", mso.intersection_of_sets(set1, set2))

    print("Difference of Set 1 - Set 2:", mso.difference_of_sets(set1, set2))

    print("Is Set 1 a subset of Set 2?:", mso.is_subset(set1, set2))
    
    print("Length of Set 1:", mso.length_of_set(set1))

    print("Symmetric Difference of Set 1 and Set 2:", mso.symmetric_difference_of_sets(set1, set2))

    print("Power Set of Set 1:", mso.power_set(set1))

    print("Unique Subsets of Set 1:", mso.unique_subsets(set1))

if __name__ == "__main__":
    demonstrate_set_operations()
