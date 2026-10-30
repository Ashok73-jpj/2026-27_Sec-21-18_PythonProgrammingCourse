x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y:  # outer: compare x with y
    if x > z:  # inner under if: compare x with z
        largest = x  # x wins
    else:
        largest = z  # z wins on this side
else:
    if y > z:  # inner under else: compare y with z
        largest = y  # y wins
    else:
        largest = z  # z wins on this side

print(f"Largest = {largest} (among {x}, {y}, {z})")
