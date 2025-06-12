def safe_divide(numerator, denominator):
    num1 = numerator
    num2 = denominator
    return num1/num2
try: 
    print(f"The result of the division is {safe_divide:.2f}")
except: 
    if denominator == 0: 
        raise ZeroDivisionError("Error: Cannot divide by zero.")
else:
    print("Error: Please enter numeric values only.") 