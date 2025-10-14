# bronzeII_1440
import sys
input = sys.stdin.readline
from itertools import permutations

D = list(map(int, input().split(':')))

count = 0
for h, m, s in permutations(D, 3):
    if 1<=h<=12 and 0<=m<=59 and 0<=s<=59:
        count += 1
print(count)