def get_weather_input():
    weather = input("What's the weather like today? (sunny/rainy/cold): ")
    return weather

def provide_clothing_recommendation(weather):
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

def main():
    weather = get_weather_input()
    provide_clothing_recommendation(weather)

if __name__ == "__main__":
    main()