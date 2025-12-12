import sys
input = sys.stdin.readline
from collections import Counter

while True:
    n, m = map(int, input().split())
    if n==m==0:
        break
    
    T = Counter(list(map(int, input().split())))
    duplicate = set()
    for num, val in T.items():
        if val > 1:
            duplicate.add(num)
    print(len(duplicate))