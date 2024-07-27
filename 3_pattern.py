def print_pyramid_pattern(n):
    
    for i in range(n):
        
        leading_spaces = ' ' * (n - i - 1)
        
        line_characters = ' '.join(chr(65 + j) for j in range(i + 1))
 
        print(leading_spaces + line_characters)

lines = 5

print_pyramid_pattern(lines)

def print_star_pyramid(n):
   
    for i in range(n):
       
        leading_spaces = ' ' * (n - i - 1)
 
        stars = '*' * (2 * i + 1)

        print(leading_spaces + stars)

lines = 5

print_star_pyramid(lines)
