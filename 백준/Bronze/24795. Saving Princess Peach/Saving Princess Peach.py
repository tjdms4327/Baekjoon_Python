import sys
input = sys.stdin.readline

n, y = map(int, input().split())
K = set([int(input()) for _ in range(y)])

for i in range(n):
    if i not in K:
        print(i)
print(f'Mario got {len(K)} of the dangerous obstacles.')