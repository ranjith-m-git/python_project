#Generate all prime number below N input from user


def is_prime_def(m):
    if m <= 1 :
        return False
    for i in range(2, int(m**0.5) + 1) :
        if m % i == 0 :
            return False
    return True



def gen_primenum_def(n):
    for i in range(2,int(n)+1):
        if is_prime_def(i) == True :
            print (f"{i} \n")

N = (input("Enter the limit to generate all prime number :\t"))
gen_primenum_def(N)

