import sys
input=sys.stdin.readline

n,k,a,b=map(int, input().split())
print((k+n-2)*b,(n-1)*a)
