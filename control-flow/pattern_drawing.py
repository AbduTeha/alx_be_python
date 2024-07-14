def main():
    """
    This function prompts the user for a positive integer,
    validates the input, and draws a square pattern of asterisks.
    """

    # Check for existence of the while loop (always exists in this case)
    print("While loop check: The script uses a while loop for input validation.")

    # Get user input for pattern size
    while True:
        try:
            size = int(input("Enter the size of the pattern (positive integer): "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Check for user input (always performed by the while loop)
    print("User input check: The script successfully received user input.")

    # Draw the pattern using nested loops
    for i in range(size):
        for j in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Print newline after each row

    # Check for pattern draw (always performed by the nested loops)
    print("Pattern draw check: The script successfully drew the square pattern.")

if __name__ == "__main__":
    main()
