import sys
input=sys.stdin.readline

n, a, b=map(int, input().split())
s=input().strip()

a-=1; b-=1
print(s[:a]+s[a:b+1][::-1]+s[b+1:])
#print(s[b:a-1:-1])