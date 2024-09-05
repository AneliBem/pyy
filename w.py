for n in range(2, 21):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'дорвнює', x, '*', n//x)
            continue
    else:
        print(n, 'просте число')