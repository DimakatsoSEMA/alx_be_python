def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError as e:
        return str(e)


    
