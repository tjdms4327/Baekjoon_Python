import sys
input = sys.stdin.readline

n, m = map(int, input().split())
v0, p0, s0 = map(int, input().split())
jae = v0+p0+s0

cand = []
for i in range(1,1+n):
    v, p, s = map(int, input().split())
    if jae < v+p+s:
        continue
    
    cand.append((v+p+s, i))

cand.sort(reverse=True)



ans = [0] + [x[1] for x in cand[:m-1]]
print(*ans)