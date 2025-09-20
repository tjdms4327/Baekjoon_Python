import sys
input = sys.stdin.readline

n, m, a = map(int, input().split())
B = list(map(int, input().split()))

penalty = 0
for i in range((n-1)*m):
    if B[i] * 2 < B[i+m]:
        penalty += a
print(penalty)