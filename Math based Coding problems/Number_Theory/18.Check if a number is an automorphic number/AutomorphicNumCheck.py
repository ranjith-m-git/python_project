

def is_automorphic_def(n) :
    num_sqr = n**2
    num_len = len(str(n))
    mod_divisor = 10**(int(num_len))

    if (num_sqr % mod_divisor) == n :
        print(f"{n} is automorphic number")
    else :
        print(f"{n} is not automorphic number")

num = int(input("Enter the number to check the number is automorphic number/not : \t"))
is_automorphic_def(num)
