

def hano(n, a, b, c):

    if n == 1:
        print(a, 'to', c)
        return None

    if n == 2:
        print(a, 'to', b)
        print(a, 'to', c)
        print(b, 'to', c)
        return None

    hano(n-1, a, c, b)
    print(a, 'to', c)

    hano(n-1, b, a, c)


hano(3, 'A', 'B', 'C')


