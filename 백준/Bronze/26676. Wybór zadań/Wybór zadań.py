import sys
input = sys.stdin.readline

from collections import Counter

n = int(input())
pos = list(input().split())

cnt = Counter(pos)
ok = True
for i in range(1, 5):
    for j in 'ABC':
        if cnt[str(i)+j] < 1:
            ok = False
for d in "ABC":
    if cnt["5"+d] < 2:
        ok = False
        
print("TAK" if ok else "NIE")