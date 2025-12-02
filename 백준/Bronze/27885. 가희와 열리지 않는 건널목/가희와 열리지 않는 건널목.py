import sys
input = sys.stdin.readline

def to_sec(t):
    h, m, s = map(int, t.split(':'))
    return 3600*h + 60*m + s

c, h = map(int, input().split()) 
intervals = []
for _ in range(c+h):
    t = to_sec(input().strip())
    intervals.append((t, t+40))
intervals.sort()

merged = []
for st, en in intervals:
    if not merged or merged[-1][1] <= st:
        merged.append([st, en])
    else:
        merged[-1][1] = max(merged[-1][1], en)
blocked = 0
for st, en in merged:
    blocked += en-st

TOTAL = 24*3600
print(TOTAL - blocked)