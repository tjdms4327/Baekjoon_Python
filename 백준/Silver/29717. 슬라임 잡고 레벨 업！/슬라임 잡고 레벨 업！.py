import sys
input=sys.stdin.readline

import math

t=int(input())
for _ in range(t):
    n=int(input())
    xp=n*(n+1)//2

    left, right=0,n
    while left<=right:
        mid=(left+right)//2
        if mid*(mid+1)<=xp:
            left=mid+1
        else:
            right=mid-1
    print(1+right)  