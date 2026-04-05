import sys, math
input = sys.stdin.readline
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

counter = Counter(A)
c1, c2, c3, c4 = counter[1], counter[2], counter[3], counter[4]

cnt = c4

temp = min(c1, c3)
cnt += temp
c3 -= temp ; cnt += c3 # 남은 3
c1 -= temp

cnt += c2//2
c2 %= 2

if c2:
    cnt += 1
    c1 -= min(c1, 2)
if c1:
    cnt += math.ceil(c1/4)
    

print(cnt)