x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x < y:  # outer: compare x with y
    if x < z:  # compare x with z
        smallest = x  # x wins
    else:
        smallest = z  # z wins on this side
else:
    if y < z:  # compare y with z
        smallest = y  # y wins
    else:
        smallest = z  # z wins on this side

print(f"Smallest = {smallest} (among {x}, {y}, {z})")
