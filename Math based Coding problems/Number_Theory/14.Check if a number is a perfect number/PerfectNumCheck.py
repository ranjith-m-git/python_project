def is_pefectnum_def(n) :
    sum_divisor = 0
    for i in range(1,(n//2)+1,1):
        if n % i == 0 :
            sum_divisor += i

    if  sum_divisor == n :
        print(f"{n} is perfect number")
    else :
        print(f"{n} isn't a perfect number")

num = int(input("Enter number to find is perfect number/ not :\t"))
is_pefectnum_def(num)
