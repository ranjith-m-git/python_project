def is_armstrong_def(num):
    num_str = str(num)               # convert number to string
    digit_count = len(num_str)       # count number of digits
    digit_calc = 0

    for digit in num_str:
        digit_calc += int(digit) ** digit_count

    if digit_calc == num:
        print(f"{num} is an Armstrong number")

    return


# Input from user
num = int(input("Enter a number to find Armstrong numbers up to it:\t"))

# Check all numbers from 1 to num
for i in range(1, num + 1):
    is_armstrong_def(i)
