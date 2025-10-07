# bronzeIII_17944
import sys
input = sys.stdin.readline

n, t = map(int, input().split())

cycle = 4 * n - 2
pos = (t - 1) % cycle + 1
if pos <= 2 * n:
    arms = pos
else:
    arms = 4 * n - pos
print(arms)