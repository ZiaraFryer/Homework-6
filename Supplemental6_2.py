# Supplemental Chapter 6 - Problem 2
# Identify a triangle from its three side lengths.

def main():
    a = float(input("Enter the first side: "))
    b = float(input("Enter the second side: "))
    c = float(input("Enter the third side: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("Invalid triangle.")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Invalid triangle.")
    elif a == b and b == c:
        print("The triangle is equilateral.")
    elif a == b or a == c or b == c:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")


main()
