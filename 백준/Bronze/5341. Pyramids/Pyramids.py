while True:
    n=int(input())
    if n != 0:
        a=[i for i in range(1,n+1)]
        print(sum(a))
    else:
        break