import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    h, m = map(int, input().split())
    if m < 45:
        m += 15
        h -= 1
    else:
        m -= 45
    if h < 0:
        h += 24
        
    print(f'Case #{case}: {h} {m}')