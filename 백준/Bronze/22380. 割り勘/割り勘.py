while True:
    n, m = map(int, input().split())
    if n+m == 0:
        break
    As = list(map(int, input().split()))

    tot=0
    for a in As:
        if a >= m//n:
            tot += m//n
        else:
            tot += a
    print(tot)