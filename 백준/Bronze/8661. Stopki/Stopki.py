import sys
input=sys.stdin.readline

x, k,a=map(int, input().split())

result=0
x-=(x//(k+a))*(k+a)
while x>=0:
    if result==0:
        x-=k
        result=1
    elif result==1:
        x-=a
        result=0
print(result)