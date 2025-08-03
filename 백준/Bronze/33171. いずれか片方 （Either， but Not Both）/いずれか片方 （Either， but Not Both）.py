import sys
input=sys.stdin.readline

n=int(input())
a=int(input())
b=int(input())



cnt=0
for i in range(1, n+1):
    if (i%a==0 and i%b!=0) or (i%b==0 and i%a!=0):
        cnt+=1
print(cnt)