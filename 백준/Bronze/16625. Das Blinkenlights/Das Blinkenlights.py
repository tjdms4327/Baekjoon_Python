# bronzeIII_16625
import sys
input = sys.stdin.readline

p, q, s = map(int, input().split())

t = [0] * (s+1)
for i in range(1, s+1):
    if i % p == 0:
        t[i] += 1
    if i % q == 0:
        t[i] += 1 
if 2 in t[1:]:
    print('yes')
else:
    print('no')