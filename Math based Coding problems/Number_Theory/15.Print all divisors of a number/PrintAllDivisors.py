
def print_all_divisor_def(n):
    for i in range(1,n+1,1):
        if n % i == 0:
            print(i, end=" ")

num = int(input("Enter the number to print all divisors:\t"))
print_all_divisor_def(num)


