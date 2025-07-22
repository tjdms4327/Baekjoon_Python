p=int(input())
for _ in range(p):
    k, n=map(int, input().split())
    print(k, n*(n+1)//2 + n)