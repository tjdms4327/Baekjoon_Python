def w(n):
    wn=0
    for i in range(n+1):
        wn+=i*((i+1)*(i+2)//2)
    return wn

t=int(input())
for _ in range(t):
    n=int(input())
    print(w(n))