a=list(map(int,input().split()))
b=list(map(int,input().split()))
asum=sum(a) ;bsum=sum(b)
if asum>=bsum:
    print(asum)
else:
    print(bsum)