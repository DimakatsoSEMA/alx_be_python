##Global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

##Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 

#User prompt
try:
    user_temp = float(input("Enter the temperature to convert: "))
    user_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if user_unit == "C":
        result = convert_to_fahrenheit(user_temp)
        print(f"{user_temp}°C is {result}°F")
    elif user_unit == "F":
        result = convert_to_celsius(user_temp)
        print(f"{user_temp}°F is {result}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")

