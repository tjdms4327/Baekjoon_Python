import sys
input=sys.stdin.readline

n,m=map(int, input().split())
trees=list(map(int, input().split()))

start, end=1, sum(trees)
while start<=end:
    cnt=0
    mid=(start+end)//2
    for tree in trees:
        if tree>mid:
            cnt+=tree-mid
    if cnt>=m:
        start=mid+1
    else:
        end=mid-1
print(end)