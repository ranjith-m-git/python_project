
def digit_sum_def(n) :
    if n == 0 :
        return 0

    digit_sum = 0
    digit = 0

    while n > 0 :
        digit = n % 10 # modulo
        digit_sum = digit_sum + digit
        n = n // 10 #integer division
    return digit_sum



num = int(input("Enter the number to sum the digits:\t"))
print(f"The sum of the digit of {num} is:\t {digit_sum_def(num)}\t")