def binary2decimal(n):
    decimal_num = 0
    reverse_n = n[::-1]
    for i in range(0,len(reverse_n),1):
       decimal_num +=  ((int(reverse_n[i])) * (2**i))

    return decimal_num

bin_str_num = input("Enter your binary input to see decimal out of it:\t")
print(f"{binary2decimal(bin_str_num)} is the decimal value of {bin_str_num}")
