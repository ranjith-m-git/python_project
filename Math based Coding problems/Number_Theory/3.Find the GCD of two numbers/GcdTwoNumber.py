
# Euclidean Algorithm is efficient method to find gcd

def gcd_def(a ,b):
    if b > a :
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


nums = list(map(int,input("Enter the GCD numbers slip by ,\t:\t ").split(',')))
print(f"GCD of {nums[0]} and {nums[1]} : {gcd_def(nums[0],nums[1])}\t")
