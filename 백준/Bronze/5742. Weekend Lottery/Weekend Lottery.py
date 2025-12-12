import sys
input = sys.stdin.readline
from collections import Counter

while True:
    n, c, k = map(int, input().split())
    if n==c==k==0:
        break
    
    nums = list(range(1, k+1))
    X = []
    for _ in range(n):
        X.extend(list(map(int, input().split())))
    count = Counter(X)
    
    if len(count) == k:
        min_count = min(count.values())
        val = [idx for idx, num in count.items() if num==min_count]
    else:
        val = [num for num in nums if num not in count]
    print(*sorted(val))