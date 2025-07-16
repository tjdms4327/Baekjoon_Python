while True:
    n=int(input())
    if n==-1: break

    miles, last_t=0,0
    for _ in range(n):
        s, t=map(int, input().split())
        miles+=(s*(t-last_t))
        last_t=t
    print(f'{miles} miles')
        