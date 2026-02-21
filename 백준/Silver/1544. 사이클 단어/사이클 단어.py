import sys
input = sys.stdin.readline

n = int(input())
s = [input().strip() for _ in range(n)]

cand = [s[0]]
for x in s[1:]:
    ok = False
    for c in cand:
        if len(c)==len(x) and c in x+x:
            ok = True
            break
    if not ok:
        cand.append(x)
        
print(len(cand))