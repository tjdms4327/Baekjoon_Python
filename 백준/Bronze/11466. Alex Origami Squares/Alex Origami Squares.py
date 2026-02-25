import sys
input = sys.stdin.readline

h, w = map(float, input().split())
if h > w:
    h, w = w, h
    
ans = max(
    min(h, w/3),
    min(h/2, w/2)
)

print(ans)