def factorial_iterative_def(n):
    if n == 0 or n == 1 :
        return 1

    result = 1
    for i in range(2,n+1):
        result *= i
    return result

num = int(input("Enter the number to find factorial:\t"))
print(f" Factorial of {num} is {factorial_iterative_def(num)}")