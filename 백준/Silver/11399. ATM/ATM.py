n=int(input())
a=list(map(int,input().split()))
a.sort()

m=0
for i in range(n):
    m+=(a[i]*(n-i))
print(m)