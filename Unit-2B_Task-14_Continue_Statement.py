n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"Skipping even number {i} with continue (N is {n})")
        continue
    print(f"for loop odd number = {i} (up to {n})")