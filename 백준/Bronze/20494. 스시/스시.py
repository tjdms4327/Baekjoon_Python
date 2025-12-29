import sys
input = sys.stdin.readline

n = int(input())

B = ''
for _ in range(n):
    B += input().strip()
print(len(B))