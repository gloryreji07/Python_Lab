# Define the dictionary with information about 10 different people
people_info = {
    "Alice": {"age": 30, "blood group": "A+"},
    "Bob": {"age": 24, "blood group": "B-"},
    "Charlie": {"age": 35, "blood group": "O+"},
    "David": {"age": 28, "blood group": "AB+"},
    "Eve": {"age": 22, "blood group": "A-"},
    "Frank": {"age": 40, "blood group": "B+"},
    "Grace": {"age": 33, "blood group": "O-"},
    "Hannah": {"age": 26, "blood group": "AB-"},
    "Ivy": {"age": 29, "blood group": "A+"},
    "Jack": {"age": 37, "blood group": "B-"}
}

def print_person_info(info):
    for name, details in info.items():
        # Print each person's name, age, and blood group
        print(f"Name: {name}")
        print(f"Age: {details['age']}")
        print(f"Blood Group: {details['blood group']}")
        # Print a line of dashes
        print('-' * 30)

# Call the function to print the information
print_person_info(people_info)
