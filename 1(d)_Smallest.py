def smallest_num_in_list(list):
    
    min = list[0]
    
    for a in list:

        if a < min:

            min = a
   
    return min


print(smallest_num_in_list([7, 3, -5, 0])) 
