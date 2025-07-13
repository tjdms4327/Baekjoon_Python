import sys
input=sys.stdin.readline

s, c, o, n=map(int, input().strip().split())
s+=n
c+=2*o
print(min(s//3, c//6))