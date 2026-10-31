rows = 5

for row in range(1, rows + 1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")
    for col in range(1, 2 * row):
        print(col, end=" ")
    print()