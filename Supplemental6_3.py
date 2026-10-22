# Supplemental Chapter 6 - Problem 3
# Classify a person's age.

def classifyAge(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def main():
    age = int(input("Enter your age: "))

    print("You are a", classifyAge(age))

    if age > 100:
        print("Congratulations on appearing on the Smucker's jar!")


main()
