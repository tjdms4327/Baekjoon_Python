import sys
input = sys.stdin.readline

s = input().strip()

cand = [s[i:] for i in range(len(s))]
for x in sorted(cand):
    print(x)