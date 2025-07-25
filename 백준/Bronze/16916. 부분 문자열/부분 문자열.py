import sys
input=sys.stdin.readline

s=input().strip()
k=input().strip()

if k in s:
    print(1)
else: print(0)