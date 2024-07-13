FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

