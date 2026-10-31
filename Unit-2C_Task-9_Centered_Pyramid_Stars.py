rows = 3

for row in range(1, rows + 1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")
    for dots in range(1, 2 * row):
        print("*", end=" ")
    print()