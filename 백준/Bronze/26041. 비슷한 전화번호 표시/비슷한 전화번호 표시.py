import sys
input=sys.stdin.readline

a=list(input().strip().split())
b=input().strip()

cnt=0
for i in a:
    if i!=b and i.startswith(b):
        cnt+=1
print(cnt)