# bronzeII_20528
import sys, math
input = sys.stdin.readline

n = int(input())
s = list(input().strip().split())

parandrom = False
for i in s:
    if s[0][0] == i[0] == i[-1]:
        parandrom = True
    else:
        parandrom = False
        break
if parandrom:
    print(1)
else:
    print(0)