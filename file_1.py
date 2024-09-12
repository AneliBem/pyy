def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(5000)




def add_numbers(num1, num2):
    sum = num1 + num2
    print('Sum:', sum)

num1 = float(input("a="))
num2 = float(input("b="))

add_numbers(num1, num2)
