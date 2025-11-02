# bronzeII_32860
import sys
input = sys.stdin.readline

n, m = input().split()
m = int(m)

if 1 <= m <= 26:
    suffix = chr(ord('A') + m - 1)
else:
    idx = m - 27  
    first = chr(ord('a') + (idx // 26))
    second = chr(ord('a') + (idx % 26))
    suffix = first + second

print(f"SN {n}{suffix}")
