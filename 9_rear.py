def extract_rear_elements(tuple_string):
   
    rear_elements = [s[-1] for s in tuple_string]
    return rear_elements

input_tuple = ("python", "lessgo", "includehelp")

output = extract_rear_elements(input_tuple)

print(output)
