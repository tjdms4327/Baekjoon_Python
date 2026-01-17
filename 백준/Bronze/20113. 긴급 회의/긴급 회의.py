import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
vote = list(map(int, input().split()))

count = Counter(vote)
max_vote = max(count.values())

cand = []
for i in range(1, n+1):
    if count[i]==max_vote:
        cand.append(i)

if len(cand)==1 and cand!=[0]:
    print(*cand)
else:
    print('skipped')