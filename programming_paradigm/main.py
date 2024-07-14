import sys
from robust_division_calculator import safe_divide

def test_safe_divide(expected_output, numerator, denominator):
    """
    Tests the safe_divide function with specific inputs and expected outputs.

    Args:
        expected_output (str): The expected output message.
        numerator (str or float): The numerator value.
        denominator (str or float): The denominator value.
    """

    result = safe_divide(numerator, denominator)
    assert result == expected_output, f"Test failed: Expected '{expected_output}', got '{result}'"

def main():
    """
    Parses command line arguments, calls safe_divide, and prints the result.
    """

    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    # Test cases for different scenarios
    test_safe_divide("The result of the division is 2.00", 10, 5)  # Normal division
    test_safe_divide("Error: Cannot divide by zero.", 10, 0)  # Division by zero
    test_safe_divide("Error: Please enter numeric values only.", "ten", 5)  # Invalid input

    main()  # Run the main function with command line arguments
