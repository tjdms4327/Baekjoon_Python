import sys
input=sys.stdin.readline

from collections import Counter

n=int(input())
a=map(int, input().strip().split())

counter=Counter(a)
for key, val in counter.items():
    if val==1:
        print(key)
        break
