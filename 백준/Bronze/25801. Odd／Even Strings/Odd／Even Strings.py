import sys
input = sys.stdin.readline

from collections import Counter

s = Counter(input().strip())
even = sum(1 for count in s.values() if count % 2 == 0)

if even == 0:
    print(1)
elif even == len(s):
    print(0)
else:
    print('0/1')