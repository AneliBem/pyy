print("Hello World")

nv = 5 - 7 * 9
print(nv)

nb = 25 ** 6
print(nb)

if nv < 0:
    print("negative")
elif nv == 0:
    print("Zero")
elif nv > 0:
    print("Positive")
for i in range(3):
    print(i, end=" ")

class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))
where_is(Point(0, 3))
where_is(Point(4, 0))
where_is(Point(5, 7))