rows = int(input("Enter the size of the pattern: "))
i = 0

while i < rows:
    j = 0
    while j < rows:
        print("*", end="")
        j += 1
    print()  # Move to the next line after printing a row
    i += 1
