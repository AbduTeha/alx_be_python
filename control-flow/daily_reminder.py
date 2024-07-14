def main():
    # Get user input for task description
    task = input("Enter your task: ")

    # Get user input for priority
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ("high", "medium", "low"):
            break
        else:
            print("Invalid priority. Please enter high, medium, or low.")

    # Get user input for time-bound status
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound not in ("yes", "no"):
        time_bound = "yes"  # Assume yes for invalid input (can be modified)

    # Process task and generate reminder
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task."
        case "low":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

    print(reminder)

if __name__ == "__main__":
    main()
