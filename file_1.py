def fib(n):

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(5000)

squares = []
for x in range(10):
    squares.append(x**2)

squares
print(squares)