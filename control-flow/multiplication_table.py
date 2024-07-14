def main():
    # Get user input for the number
    number = int(input("Enter a number to see its multiplication table: "))

    # Print the multiplication table header
    print(f"Multiplication table of {number}:")

    # Generate and print the table using a for loop
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
