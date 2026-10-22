# Supplemental Chapter 6 - Problem 1
# Check x before running the chaos calculation.

def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


def main():
    x = float(input("Enter a number between 0 and 1: "))

    if x < 0 or x > 1:
        print("Error: Number must be between 0 and 1.")
        return

    k = float(input("Enter a value for k: "))
    chaos(k, x, 30)


main()
