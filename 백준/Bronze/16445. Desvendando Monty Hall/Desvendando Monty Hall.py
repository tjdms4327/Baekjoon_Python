import sys
input=sys.stdin.readline

n=int(input())
lst=[input().strip() for _ in range(n)]
print(n-lst.count('1'))