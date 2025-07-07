a=list(map(int,input().split()))
tot=a[-1]*len(a[:-1])
st=sum(a[:-1])
if tot<=st:
    print(0)
else:
    print(tot-sum(a[:-1]))