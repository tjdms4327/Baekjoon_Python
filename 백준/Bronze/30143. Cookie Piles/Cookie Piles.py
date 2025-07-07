t=int(input())
for _ in range(t):
    n,a,d=map(int, input().split())
    print(n*a+n*d*(n-1)//2)