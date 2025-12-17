def sum_N_natural_num(num):
    """
    Gauss formula -- efficient method :
    sum of first N natural number = (N * (N + 1)) /2
    """
    sum = 0
    sum = (num * (num + 1)) / 2

    return sum

num = int(input("Enter the number to sum of natural number: "))
print(f"sum of {num} natural number is: {sum_N_natural_num(num)}")