def print_even_squares(start, end):
    print(f"Even numbers and their squares in the range({start}, {end}):")
    # Iterate through the range
    for number in range(start, end):
        # Check if the number is even
        if number % 2 == 0:
            # Calculate the square of the number
            square = number ** 2
            # Print the number and its square
            print(f"{number} -> {square}")

# Define the ranges
range1 = (1, 50)
range2 = (1, 100)

# Call the function for each range
print_even_squares(*range1)
print()
print_even_squares(*range2)
