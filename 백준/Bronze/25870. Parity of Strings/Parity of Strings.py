import sys
input = sys.stdin.readline

from collections import Counter

s = Counter(input().strip())
even = sum(1 for val in s.values() if val%2==0)

if even == len(s):
    print(0)
elif even == 0:
    print(1)
else:
    print(2)