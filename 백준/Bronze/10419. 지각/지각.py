t=int(input())
for _ in range(t):
    d=int(input())
    t=int(d**0.5)
    while t**2+t>d:
        if t==0:
            break
        t-=1
    print(t)
    