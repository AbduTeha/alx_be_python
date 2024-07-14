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

def main():
    size = get_pattern_size()
    draw_pattern(size)

if __name__ == "__main__":
    main()