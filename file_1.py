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



i = 5

def f(arg=i):
    print(arg)

i = 6
f()

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Ви дійсно хочете вийти?')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))

print(fruits.count('tangerine'))

print(fruits.index('banana'))

print(fruits.index('banana', 4))

fruits.reverse()
print(fruits)

fruits.append('grape')
fruits

fruits.sort()
fruits
print(fruits.pop())


stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack
print(stack)
stack.pop()
stack
print(stack)
stack.pop()
stack.pop()
stack
print(stack)


