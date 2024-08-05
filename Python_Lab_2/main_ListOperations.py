import module_ListFunction as mlf

def demonstrate_functions():
    
    list1 = [5, 3, 8, 1, 9]
    list2 = [7, 2, 1, 8, 3, 4, 5]
    list3 = [10, 15, 25, 35, 45, 55]

    print("List 1:", list1)
    print("List 2:", list2)
    print("List 3:", list3)
    
    print("Maximum of List 1:", mlf.find_max(list1))
    print("Maximum of List 2:", mlf.find_max(list2))
    
    print("Minimum of List 1:", mlf.find_min(list1))
    print("Minimum of List 2:", mlf.find_min(list2))
    
    print("Sum of List 1:", mlf.calculate_sum(list1))
    print("Sum of List 2:", mlf.calculate_sum(list2))
    
    print("Average of List 1:", mlf.calculate_average(list1))
    print("Average of List 2:", mlf.calculate_average(list2))
    
    print("Median of List 1:", mlf.find_median(list1))
    print("Median of List 2:", mlf.find_median(list2))
    print("Median of List 3:", mlf.find_median(list3))

if __name__ == "__main__":
    demonstrate_functions()
