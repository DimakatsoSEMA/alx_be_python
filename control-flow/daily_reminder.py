task_description = input("Enter your task: ").lower()
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" if time_bound == "yes": 
        print(f"Reminder: {task_description} is a high priority task that requires immediate attention today!")
    case "medium" if time_bound == "yes":
        print(f"Note: {task_description} is a low priority task and does not require a lot of time.")
    case "low" if time_bound == "no":
        print(f"Note: {task_description} is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"{task_description} is not too important ")

      


