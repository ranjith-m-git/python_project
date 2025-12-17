
def count_num_divisor_def(n):
    divisor_count = 0
    for i in range (1,n+1):
        if n % i == 0 :
            divisor_count += 1

    return divisor_count

num = int(input("Enter the number to finds divisors:\t"))
print(f" {count_num_divisor_def(num)} number divisor for {num}")
