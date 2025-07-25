import sys
input=sys.stdin.readline

s=input().strip()
filtered=''.join(i for i in s if i.isalpha())
k=input().strip()

if k in filtered:
    print(1)
else: print(0)