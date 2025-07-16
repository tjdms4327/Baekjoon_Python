while True:
    try:
        n, w, d, measured=map(int, input().split())
        ideal=((n-1)*n//2)*w
        if measured==ideal: print(n)
        else:
            print((ideal-measured)//d)
    except EOFError:
        break