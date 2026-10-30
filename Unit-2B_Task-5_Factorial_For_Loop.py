number = int(input("Enter a number: "))


factorial = 1  # start with 1

for i in range(1, number + 1):  # values from 1 to number
    factorial = factorial * i  # multiply factorial by current value

print(f"Factorial of {number} is {factorial}")