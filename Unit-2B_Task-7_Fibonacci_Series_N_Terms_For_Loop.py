n = int(input("Enter how many terms: "))


first = 0
second = 1

for i in range(n):
    print(f"Fibonacci series term {i + 1} of {n} terms = {first}")
    next_term = first + second
    first = second
    second = next_term