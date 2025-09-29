# bronzeII_11094
import sys, math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().strip()
    if s[:10] == 'Simon says':
        print(s[10:])