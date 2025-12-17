
def is_armstrong_def(num) :
    digit_count = len(num)
    num_int = int(num)
    digit_calc = 0

    for i in range(0,digit_count,1) :
        digit_calc += ((int(num[i]))**digit_count)

    if digit_calc == num_int :
        print(f"{num} is Armstrong number")




num = input("Enter the number to check it is Armstrong NUM :\t")
is_armstrong_def(num)