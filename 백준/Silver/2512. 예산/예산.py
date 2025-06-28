import sys
input=sys.stdin.readline

n=int(input())
requests=list(map(int, input().split()))
tot=int(input())

start, end=0, max(requests)
while start<=end:
    most=0
    mid=(start+end)//2
    for quest in requests:
        if quest<=mid:
            most+=quest
        else:
            most+=mid
    if most>tot:
        end=mid-1
    else:
        start=mid+1
print(end)