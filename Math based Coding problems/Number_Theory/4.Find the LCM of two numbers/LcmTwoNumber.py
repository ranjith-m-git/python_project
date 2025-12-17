def lcm_def(a,b) :
    lcm = (a*b) // gcd_def(a,b) # integer division
    lcm = int(lcm)
    return lcm

def gcd_def(a,b) :
    if b > a :
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

nums = list(map(int,input("Enter LCM Two numbers :\t").split(',')))
print(f"LCM of {nums[0]} and {nums[1]} : {lcm_def(nums[0],nums[1])} ")