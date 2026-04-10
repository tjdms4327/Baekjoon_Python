import sys
input = sys.stdin.readline
import bisect

m, n, l = map(int, input().split())
guns = list(map(int, input().split()))
guns.sort()

coord = [tuple(map(int, input().split())) for _ in range(n)]

cnt = 0
for a, b in coord:
    if b > l:
        continue
    
    r = l-b
    idx = bisect.bisect_left(guns, a)
    if idx<m and abs(guns[idx]-a) <= r:
        cnt += 1
    elif idx > 0 and abs(guns[idx-1]-a) <= r:
        cnt += 1
    
print(cnt)

