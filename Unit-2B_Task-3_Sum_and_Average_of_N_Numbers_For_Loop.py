total_input_numbers = int(input("Enter how many numbers: "))
total_sum = 0  # start with zero

for x in range(total_input_numbers):  # repeat total_input_numbers times (use range)
    enter= float(input("Enter a number: "))  # read each number
    total_sum += enter  # add the number to total_sum

average =total_sum/total_input_numbers  # divide total_sum by total_input_numbers

print(f"Sum of {total_input_numbers} numbers is {total_sum}")
print(f"Average of {total_input_numbers} numbers (sum {total_sum}) is {average}")