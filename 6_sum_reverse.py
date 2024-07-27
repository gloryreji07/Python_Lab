def sum_of_digits(number):
    
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
 
    return int(str(number)[::-1])

def main():
    
    while True:
        try:
            number = int(input("Enter a four-digit number: "))
            
            if 1000 <= number <= 9999:
                break
            else:
                print("Please enter a valid four-digit number.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    sum_digits = sum_of_digits(number)
    reversed_number = reverse_number(number)
    

    print(f"Sum of digits: {sum_digits}")
    print(f"Reverse of the number: {reversed_number}")


if __name__ == "__main__":
    main()
