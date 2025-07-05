import sys
input=sys.stdin.readline

kans=list(map(int, input().split()))

length=max(kans[2]-kans[1], kans[1]-kans[0])
print(length-1)
