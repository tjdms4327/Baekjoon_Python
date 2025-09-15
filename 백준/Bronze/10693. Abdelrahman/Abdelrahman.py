import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    n, m = map(int, input().split())
    print(f'Case {case}: {m - n + 1}')