import sys
input = sys.stdin.readline

n = int(input())

cand = set()
for a in range(1, int(n**0.5)+1):
    b = n//a
    if a*b == n:
        cand.add((a, b))
        cand.add((b, a))
print(len(cand))