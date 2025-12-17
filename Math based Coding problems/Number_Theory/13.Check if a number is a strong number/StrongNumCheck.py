def factorial_iterative_def(n):
    if n == 0 or n == 1 :
        return 1

    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def is_strong_num_def(num) :
    sum_digits = 0
    for i in range(0,(len(num)),1):
        sum_digits += factorial_iterative_def(int(num[i]))

    if sum_digits == int(num):
        print (f"{num} is strong number")
    else :
        print (f"{num} is not a strong number ")


num = input("Enter Number is to check is StrongNum/not :\t")
is_strong_num_def(num)