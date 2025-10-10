# bronzeIII_15354
import sys
input = sys.stdin.readline
from itertools import groupby

n = int(input())
people = list(input().strip() for _ in range(n))

group = [key for key, _ in groupby(people)]
print(len(group) + 1)