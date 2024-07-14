def main():
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

    # Draw the pattern using nested loops
    for i in range(size):
        for j in range(size):
            print("*", end="")  # Print asterisk without newline
        print()  # Print newline after each row

if __name__ == "__main__":
    main()
