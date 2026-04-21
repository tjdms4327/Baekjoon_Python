import sys
input = sys.stdin.readline

u, o, s = map(int, input().split())

res = min(u, o, s)

k = (u-s) // 3
for dk in range(-2, 3):
    nk = k + dk
    if 0 <= nk <= u//2:
        res = max(res, min(u - 2*nk, o, s + nk))
        
print(res)