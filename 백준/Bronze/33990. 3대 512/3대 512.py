import sys
input=sys.stdin.readline

n=int(input().strip())
cand=-1
for _ in range(n):
    a, b, c=map(int, input().strip().split())
    tot=a+b+c
    if tot>=512:
        if (tot-512)<abs(cand-512): # abs는 cand=-1일 때 때문
            cand=tot
print(cand)