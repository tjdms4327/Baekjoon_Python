import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    print(f'Case {i}:')

    n = int(input())
    for i in range(1, 7):
        if 1 <= n-i <= 6 and i <= n-i:
            print(f'({i},{n-i})')