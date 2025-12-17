def fibonacci_nth_num_gen(num):
    first = 0
    second = 1
    for i in range(0,num,1):
        first, second = second, first + second
    return first

num = int(input("Enter the number to find the nth: "))
print(f" {num}th of fibonaci number is : {fibonacci_nth_num_gen(num)}")
