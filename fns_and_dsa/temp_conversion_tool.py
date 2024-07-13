FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The converted temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The converted temperature in Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
            break
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        converted_unit = 'F'
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        converted_unit = 'C'
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
        return

    print(f"{temperature:.1f}°{unit} is {converted_temp:.1f}°{converted_unit}")


if __name__ == "__main__":
    main()
