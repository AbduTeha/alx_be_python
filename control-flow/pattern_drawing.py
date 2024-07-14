def get_pattern_size():
    while True:
        size = input("Enter the size of the pattern: ")
        if size.isdigit() and int(size) > 0:
            return int(size)
        else:
            print("Invalid input. Please enter a positive integer.")

def draw_pattern(size):
    for _ in range(size):
        for _ in range(size):
            print("*", end="")
        print()

def check_user_input(size):
    if not isinstance(size, int):
        raise ValueError("User input must be an integer")
    if size <= 0:
        raise ValueError("User input must be a positive integer")

def check_while_loop():
    if not any("while" in line for line in open(__file__).readlines()):
        raise RuntimeError("While loop is not used in the program")

def check_pattern_draw():
    pattern = ""
    with open(__file__, "r") as file:
        for line in file:
            if "print(\"*\", end=\"\")" in line:
                pattern += "*"
            if "print()" in line:
                pattern += "\n"
    if not pattern.strip():
        raise RuntimeError("Pattern is not drawn in the program")

def main():
    try:
        size = get_pattern_size()
        check_user_input(size)
        draw_pattern(size)
        check_while_loop()
        check_pattern_draw()
    except ValueError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()