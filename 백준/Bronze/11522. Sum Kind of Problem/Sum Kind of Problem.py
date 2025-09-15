import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, n = map(int, input().split())
    s1 = sum(range(1, n+1))
    s2 = sum(range(1, 2 * n, 2))
    s3 = sum(range(2, 2 * n + 1, 2))
    print(f'{k} {s1} {s2} {s3}')