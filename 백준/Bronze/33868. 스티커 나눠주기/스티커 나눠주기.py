import sys
input=sys.stdin.readline

n=int(input().strip())
cand_t, cand_b=0, 5001
for _ in range(n):
    t, b=map(int, input().strip().split())
    if cand_t<t: cand_t=t
    if cand_b>b: cand_b=b
print((cand_t*cand_b)%7 + 1)