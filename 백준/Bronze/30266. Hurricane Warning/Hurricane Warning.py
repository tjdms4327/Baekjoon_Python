import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    n = int(input())
    media = set(input().strip())
    cnt = 0
    for _ in range(n):
        s = input().strip()
        if any(ch in s for ch in media):
            cnt += 1
    print(f'Data Set {case}:')
    print(cnt)
    print()