import sys
input=sys.stdin.readline

start, end, d=map(int, input().split())
cnt=0
for i in range(start, end+1):
    i=str(i)
    cnt+=i.count(str(d))
print(cnt)