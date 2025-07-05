n,m=map(int,input().split())

a=[]
for i in range(2*n):
    nums=map(int,input().split())
    a.append(list(nums))

for j in range(n):
    d=''
    for k in range(m):
        b=a[j][k]+a[j+n][k]
        d+=(str(b)+' ')
    print(d)