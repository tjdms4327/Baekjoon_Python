import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

if n==1 or m==1:
    print(0)
else:
    print((n-1)*(m-1)*2)