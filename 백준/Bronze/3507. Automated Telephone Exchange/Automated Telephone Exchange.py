import sys
input=sys.stdin.readline

n=int(input().strip())
cnt=0
for a in range(100): # 00부터 99
    b=n-a
    if 00<=b<=99: cnt+=1
print(cnt)