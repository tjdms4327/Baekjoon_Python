# bronzeII_31533
import sys
input = sys.stdin.readline

a = int(input())
m, n = map(int, input().split())

if m > n:
    cand1, cand2 = m, n/a
else:
    cand1, cand2 = m/a, n
print(min(max(cand1, cand2), cand1*2, cand2*2))