rows = int(input("Enter number of rows: "))

for row in range(1, rows + 1):
    for spaces in range(1, rows - row + 1):
        print(" ", end="")

    value = 1

    for col in range(1, row + 1):
        print(value, end=" ")
        value = value * (row - col) // col

    print()