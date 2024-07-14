weather_options = ["sunny", "rainy", "cold"]  # List of valid weather conditions

# Get user input
user_input = input("What's the weather like today? (sunny/rainy/cold): ").lower()  # Convert to lowercase

# Check weather conditions and provide recommendations
if user_input in weather_options:
    if user_input == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif user_input == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    else:  # user_input == "cold"
        print("Make sure to wear a warm coat and a scarf.")
else:
    print(f"Sorry, I don't have recommendations for '{user_input}' weather.")
