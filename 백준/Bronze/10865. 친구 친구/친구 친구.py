import sys
input = sys.stdin.readline

n, m = map(int, input().split())

friend = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    friend[a] += 1
    friend[b] += 1
    
for i in friend[1:]:
    print(i)