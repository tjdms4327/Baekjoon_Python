import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    s = list(input().strip().split())
    print(f'Case {case}: ', end = '')
    a, b, c = int(s[0]), int(s[2]), int(s[4])
    if s[1] == '+' and a+b == c:
        print('YES')
    elif s[1] == '-' and a-b == c:
        print('YES')
    else:
        print('NO')