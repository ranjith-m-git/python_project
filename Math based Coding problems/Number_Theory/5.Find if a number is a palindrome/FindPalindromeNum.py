
def is_Palindrome_def(num) :
    num_temp = num
    reverse_num = 0

    while num_temp > 0 :
        reverse_digit = num_temp % 10
        reverse_num = reverse_num * 10 + reverse_digit
        num_temp = num_temp // 10

    if reverse_num == num :
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")

num = int(input("Enter the number to check it is palindrome/not :\t"))
is_Palindrome_def(num)