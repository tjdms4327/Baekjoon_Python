import sys
input = sys.stdin.readline

H = list(map(int, input().split()))
S = list(map(int, input().split()))
V = list(map(int, input().split()))
r, g, b = list(map(int, input().split()))

M, m = max(r,g,b), min(r,g,b)
v = M
s = 255 * (v - m) / v
if v == r:
    h = (60 * (g - b) / (v - m))
elif v == g:
    h = 120 + (60 * (b - r) / (v - m))
else:
    h = 240 + (60 * (r - g) / (v - m))
if h < 0:
    h += 360

if (H[0] <= h <= H[1]) and (S[0] <= s <= S[1]) and (V[0] <= v <= V[1]):
    print('Lumi will like it.')
else:
    print('Lumi will not like it.')