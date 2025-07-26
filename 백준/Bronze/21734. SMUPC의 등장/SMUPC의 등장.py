import sys
input=sys.stdin.readline

s=input().strip()
for i in s:
    cnt=sum(map(int, str(ord(i))))
    print(i*cnt)
