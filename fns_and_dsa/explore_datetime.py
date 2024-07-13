from datetime import datetime, timedelta


def display_current_datetime():
    """
    Gets the current date and time and prints it in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days):
    """
    Calculates the future date by adding a specified number of days to the current date.

    Args:
        days (int): The number of days to add to the current date.

    Returns:
        datetime: The future date object.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date


def main():
    display_current_datetime()

    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    future_date = calculate_future_date(days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    main()
