# bronzeII_32751
import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d = map(int, input().split())
s = input().strip()

prev = ''
for i in range(n):
    if (i == 0 or i == n - 1) and s[i] != 'a':
        print('No')
        sys.exit()

    if s[i] == prev:
        print('No')
        sys.exit()

    if s[i] == 'a': a -= 1
    elif s[i] == 'b': b -= 1
    elif s[i] == 'c': c -= 1
    elif s[i] == 'd': d -= 1
    else:
        print('No')
        sys.exit()

    if min(a, b, c, d) < 0:
        print('No')
        sys.exit()

    prev = s[i]

print('Yes')
