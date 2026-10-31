rows = int(input("Enter number of rows: "))

for row in range(rows, 0, -1):
    for col in range(1, row + 1):
        print("*", end=" ")
    print()