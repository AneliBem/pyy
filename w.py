for n in range(2, 21):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'дорвнює', x, '*', n//x)
            continue
    else:
        print(n, 'просте число')

a = 6
match a:
    case 1:
         print("Один")
    case 2:
        print("Два")
    case 4:
        print("Чотири")
    case _:
        print("Інше число")