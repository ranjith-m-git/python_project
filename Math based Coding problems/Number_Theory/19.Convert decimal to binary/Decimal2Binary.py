def decimal2binary_def(n):
    binary_num = ""  # will store binary digits as a string
    while n != 0:
        remainder = n % 2
        binary_num += str(remainder)  # append remainder to string
        n = n // 2
    return binary_num[::-1]  # reverse the string before returning

num = int(input("Enter any decimal number to get its binary number:\t"))
print(f"Binary representation: {decimal2binary_def(num)}")
