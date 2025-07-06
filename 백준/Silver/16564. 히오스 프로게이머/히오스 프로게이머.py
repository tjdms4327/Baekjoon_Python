import sys
input=sys.stdin.readline

xs=[]
n,k=map(int, input().split())
for _ in range(n):
    xs.append(int(input()))
xs.sort()

low, high=xs[0], xs[0]+k
while low<=high:
    mid=(low+high)//2
    require=0
    for x in xs:
        if x<mid:
            require+=mid-x
    if require<=k:
        low=mid+1
    else:
        high=mid-1
print(high)