import sys
from robust_division_calculator import safe_divide

def main():
    """
    Parses command line arguments and calls the safe_divide function for division.
    """

    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
