def safe_divide(numerator, denominator):
    """
    Perform division, handling potential errors:
    - Division by Zero: Catch ZeroDivisionError
    - Non-numeric Input: Catch ValueError for non-numeric inputs
    Return appropriate messages for errors or the result for successful division.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return "Error: Cannot divide by zero."
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."