from math import pi
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

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))

combs
print(combs)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print([str(round(pi, i)) for i in range(1, 6)])#1

print([[row[i] for row in matrix] for i in range(4)]) #2

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed) #3

print(list(zip(*matrix)))#4