# bronzeII_21567
import sys
input = sys.stdin.readline
from collections import Counter

a = int(input())
b = int(input())
c = int(input())

result = Counter(str(a*b*c))
for i in range(10):
    print(result[str(i)])