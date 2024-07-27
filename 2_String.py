A = ['abc', 'xyz', 'aba', '1221']

for index, string in enumerate(A):

    if len(string) > 0 and string[0] == string[-1]:
        
        print(f"Index: {index}, String: {string}")
