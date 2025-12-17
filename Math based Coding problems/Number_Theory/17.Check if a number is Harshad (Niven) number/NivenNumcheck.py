
def is_niven_num_def(num):
    sum_digit = 0
    int_num = int(num)

    for i in range(0,len(num),1):
        sum_digit += int(num[i])

    if int_num % sum_digit == 0:
        print("It is Niven Number \n")
    else :
        print("It is not Niven Number\n")



num = input("Enter the number to check it is Niven num/not : \t")
is_niven_num_def(num)