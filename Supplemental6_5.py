# Supplemental Chapter 6 - Problem 5
# Check whether a number has a factor between 2 and n - 1.

def checkPrime(n):
    found = False

    for i in range(2, n):
        if n % i == 0:
            found = True

    return found


def main():
    n = int(input("Enter an integer: "))

    if n < 2:
        print(n, "is not a prime number.")
    elif checkPrime(n):
        print(n, "is not a prime number.")
    else:
        print(n, "is a prime number.")


main()
