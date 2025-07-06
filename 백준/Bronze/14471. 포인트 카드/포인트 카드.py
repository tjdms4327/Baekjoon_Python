n,m=map(int, input().split())

ab=[]
for _ in range(m):
    a,b=map(int, input().split())
    if a<(n):
        ab.append(n-a)
ab.sort()
print(sum(ab[:-1]))