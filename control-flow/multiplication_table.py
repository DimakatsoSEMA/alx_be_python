user = int(input("Enter a number to see its multiplication table: "))

for i in range(1,11):
    result = user * i
    print(f"{user} x {i} = {result}")
