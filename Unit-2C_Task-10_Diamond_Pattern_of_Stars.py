rows = int(input("Enter number of rows (half diamond): "))

# Upper half (including middle)
for row in range(1, rows + 1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")
    for dots in range(1, 2 * row):
        print("*", end=" ")
    print()

# Lower half
for row in range(rows - 1, 0, -1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")
    for dots in range(1, 2 * row):
        print("*", end=" ")
    print()
    