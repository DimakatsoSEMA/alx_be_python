###Display the current date and time 
def display_current_datetime():
    from datetime import datetime
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted)

display_current_datetime()

##Calculate future date
def calculate_future_date(days):
    from datetime import datetime , timedelta
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")
##Promt user
try:
    user_days = int(input("Enter the number of days to add to the current date: "))
    result = calculate_future_date(user_days)
    print("Future date: ", result)

except ValueError:
    print("Please enter a valid integer.")

calculate_future_date(user_days)