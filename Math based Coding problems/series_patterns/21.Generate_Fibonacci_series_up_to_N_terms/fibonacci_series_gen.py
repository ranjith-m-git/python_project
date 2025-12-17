
def fibonacci_iterative_def(num):
    series = []
    first = 0
    second = 1
    for i in range(0,num,1):
        series.append(first)
        first, second = second, first + second
    return series

num = int(input("Enter the fibonacci number: "))
print(f"Generated the {num} series : {fibonacci_iterative_def(num)}")