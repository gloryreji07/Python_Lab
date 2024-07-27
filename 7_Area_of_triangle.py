import math

def calculate_area(a, b, c):
    # Compute the semi-perimeter
    s = (a + b + c) / 2
    # Compute the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    print("Enter the sides of the first triangle:")
    # Read the sides of the first triangle
    a1 = float(input("Side a1: "))
    b1 = float(input("Side b1: "))
    c1 = float(input("Side c1: "))
    
    print("Enter the sides of the second triangle:")
    # Read the sides of the second triangle
    a2 = float(input("Side a2: "))
    b2 = float(input("Side b2: "))
    c2 = float(input("Side c2: "))
    
    # Calculate the area of each triangle
    area1 = calculate_area(a1, b1, c1)
    area2 = calculate_area(a2, b2, c2)
    
    # Compute total area
    total_area = area1 + area2
    
    # Calculate each triangle's contribution percentage
    contribution1 = (area1 / total_area) * 100
    contribution2 = (area2 / total_area) * 100
    
    # Print results
    print(f"\nArea of the first triangle: {area1:.2f}")
    print(f"Area of the second triangle: {area2:.2f}")
    print(f"Total area enclosed by both triangles: {total_area:.2f}")
    print(f"First triangle's contribution: {contribution1:.2f}%")
    print(f"Second triangle's contribution: {contribution2:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()
