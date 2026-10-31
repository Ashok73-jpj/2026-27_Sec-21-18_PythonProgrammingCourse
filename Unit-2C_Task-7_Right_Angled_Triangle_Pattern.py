rows = int(input("Enter number of rows: "))
symbol = input("Enter symbol to print (e.g. * or 0): ")

for row in range(1, rows + 1):
    for col in range(1, row + 1):
        print(symbol, end=" ")
    print()