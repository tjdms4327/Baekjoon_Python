import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
pos = [0] + list(map(int, input().split())) + [l] # 양 끝값 포함
pos.sort()

gaps = []
for i in range(len(pos)-1):
    gaps.append(pos[i+1]-pos[i])
    


def possible(x):
    cnt = 0
    for g in gaps:
        cnt += (g-1) // x
    return cnt <= m

left, right = 1, l
ans = 0
while left <= right:
    mid = (left+right)//2
    if possible(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(ans)