# Prompt the user for monthly income
monthly_income = int(input("Enter your monthly income: "))
print(f"Your monthly income is: {monthly_income}")

# Prompt the user for monthly expenses (renamed from total_monthly_expenses)
monthly_expenses = int(input("Enter your total monthly expenses: "))
print(f"Your total monthly expenses are: {monthly_expenses}")

# Monthly savings (this line must match the expected pattern)
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: {monthly_savings}")

# Projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {projected_savings}")

