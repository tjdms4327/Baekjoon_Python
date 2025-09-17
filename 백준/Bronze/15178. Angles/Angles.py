import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    angles = list(map(int, input().split()))
    if sum(angles) == 180:
        print(*angles, 'Seems OK')
    else:
        print(*angles, 'Check')