# bronzeI_1855
import sys
input = sys.stdin.readline

col_num = int(input())
s = input().strip()

original = []
for i in range(0, len(s), col_num):
    part = s[i:i+col_num]
    if (i // col_num) % 2 == 1:
        part = part[::-1]
    original.append(part)

for row in zip(*original):
    print(''.join(row), end='')