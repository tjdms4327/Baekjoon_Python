import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (100*y) // x

if z >= 99:
    print(-1)
    sys.exit()
    
left, right = 1, 10**9
while left <= right:
    mid = (left+right) // 2
    
    if (100*(y+mid)) // (x+mid) <= z:
        left = mid + 1
    else:
        right = mid - 1
        
print(left)