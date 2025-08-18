import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d, n, s, p = map(int, input().split())


    if d + (p * n) == s * n:
        print('does not matter')
    elif d + (p * n) < s * n:
        print('parallelize')
    else:
        print('do not parallelize')