def count_digits_def(num) :
    digit_count = 0
    if num == 0 :
        return 0
    while num > 0 :
        num = num // 10 #integer division
        digit_count += 1
    return digit_count

num = int(input("Enter the Number to count its digits:\t"))
print(f"Digit count of the {num} is : {count_digits_def(num)}\t")