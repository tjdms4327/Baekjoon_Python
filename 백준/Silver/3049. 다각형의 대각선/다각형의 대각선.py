import sys
input = sys.stdin.readline

n = int(input())

ans = n*(n-1)*(n-2)*(n-3)//(4*3*2)
print(ans)