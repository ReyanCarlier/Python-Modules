import sys

def main():
    if (len(sys.argv) != 3):
        print("Invalid arguments. Usage : python3 operations.py <int> <int>")
        return
    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        print("Sum:", A+B)
        print("Difference:", A-B)
        print("Product:", A*B)
        if (B == 0):
            print("Quotient: ERROR (division by zero)")
            print("Remainder: ERROR (modulo by zero)")
        else:
            print("Quotient:", A/B)
            print("Remainder:", A%B)
    except ValueError:
        print("ValueError: Arguments are not integer")
        return

if (__name__ == "__main__"):
    main()