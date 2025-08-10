import sys
input=sys.stdin.readline

import math

t=int(input())
for _ in range(t):
    x,w=map(int, input().split())
    if w<=x:
        ans=0
    else:
        ans=math.ceil(math.log2(w/x))
    print(ans)