import sys
input = sys.stdin.readline

for case in range(1, int(input()) + 1):
    n, w, e = map(int, input().split())
    
    total = 0
    for _ in range(n):
        ww, we, ew, ee = map(int, input().split())
        west_version = w * ww + e * ew
        east_version = w * we + e * ee
        total += max(west_version, east_version)
    print(f'Data Set {case}:\n{total}\n')