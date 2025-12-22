import sys
input = sys.stdin.readline

s = input().strip()

ucpc = 0
for ch in s:
    if ucpc == 0:
        if ch == 'U':
            ucpc += 1
    elif ucpc == 1 or ucpc == 3:
        if ch == 'C':
            ucpc += 1
    elif ucpc == 2:
        if ch =='P':
            ucpc += 1

if ucpc == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')