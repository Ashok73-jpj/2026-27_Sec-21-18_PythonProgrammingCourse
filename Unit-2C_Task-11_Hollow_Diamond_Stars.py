rows = 3

# Upper half
for row in range(1, rows + 1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")

    for col in range(1, 2 * row):
        if col == 1 or col == 2 * row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Lower half
for row in range(rows - 1, 0, -1):
    for spaces in range(1, rows - row + 1):
        print(" ", end=" ")

    for col in range(1, 2 * row):
        if col == 1 or col == 2 * row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()