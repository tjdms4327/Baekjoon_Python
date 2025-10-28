# bronzeI_16495
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s) - 1

col_num = 0
for ch in s:
    cur = ord(ch) - ord('A') + 1
    col_num += 26**n * cur
    n -= 1
print(col_num)