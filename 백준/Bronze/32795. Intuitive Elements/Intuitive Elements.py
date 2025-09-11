import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = input().strip()
    b = input().strip()

    if set(b).issubset(set(a)):
        print('YES')
    else:
        print('NO')