
def find_trailing_zero_def(num):
    tc_counter = 0
    i = 5
    while num//i > 0:
        tc_counter += num // i
        i *= 5
    return tc_counter

num = int(input("Enter the number to find trailing zero of factorial of given number:\t"))
print(f"Number of Trailing zeros : {find_trailing_zero_def(num)}")
