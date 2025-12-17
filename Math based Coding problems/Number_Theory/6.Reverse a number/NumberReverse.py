
def reverse_num_def(num):
    temp_num = num
    reversed_num = 0 
    while temp_num > 0 :
        reverse_digit = temp_num % 10
        reversed_num = (reversed_num * 10) + reverse_digit
        temp_num = temp_num // 10 # integer division

    return reversed_num

num = int(input("Enter a number to reverse:\t"))
print(f"Reverse of given number {num} is :\t{reverse_num_def(num)}\t")