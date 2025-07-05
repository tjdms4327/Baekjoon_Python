n,m=map(int,input().split())
a=list(map(int,input().split()))

b=[]
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            M=a[i]+a[j]+a[k]
            if M<=m:
                b.append(M)
print(sorted(b)[-1])