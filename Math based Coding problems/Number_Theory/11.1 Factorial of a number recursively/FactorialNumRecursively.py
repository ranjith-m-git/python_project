def factorial_iterative_def(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_iterative_def(n-1)


num = int(input("Enter the number to find factorial:\t"))
print(f" Factorial of {num} is {factorial_iterative_def(num)}")