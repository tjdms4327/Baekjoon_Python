# bronzeI_25183
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

lotto, cur_len = -1, 1
prev = s[0]
for ch in s[1:]:
    if abs(ord(ch) - ord(prev)) == 1:
        cur_len += 1
    else:
        cur_len = 1
    prev = ch
    lotto = max(lotto, cur_len)

if lotto >= 5:
    print('YES')
else:
    print('NO')