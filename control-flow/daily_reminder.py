Task= input("Enter your task: ").lower()
Priority = input("Priority (high, medium, low): ").lower()
Time_bound = input("Is it time-bound? (yes/no): ").lower()

match Priority:
    case "high" if Time_bound == "yes": 
        print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
    case "medium" if Time_bound == "yes":
        print(f"Note: {Task} is a low priority task and does not require a lot of time.")
    case "low" if Time_bound == "no":
        print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"{Task} is not too important ")

      


