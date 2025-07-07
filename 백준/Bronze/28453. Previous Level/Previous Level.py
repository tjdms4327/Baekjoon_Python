n=int(input())
m=list(map(int, input().split()))

for i in range(n):
    if m[i]>=300:
        m[i]=1
    elif m[i]>=275:
        m[i]=2
    elif m[i]>=250:
        m[i]=3
    else:
        m[i]=4
print(*m, sep=' ')