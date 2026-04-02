import sys, math
input = sys.stdin.readline

rh, rv, sh, sv = map(int, input().split())
n = int(input())

ans = float('inf')
for _ in range(n):
    rhi, rvi, shi, svi, p = map(int, input().split())
    
    for _ in range(2):
        a = max(math.ceil(rh/rhi), math.ceil(sh/shi))
        b = max(math.ceil(rv/rvi), math.ceil(sv/svi))
        
        cost = a*b*p
        ans = min(ans, cost)
        
        # 회전
        rhi, rvi = rvi, rhi
        shi, svi= svi, shi
        
print(ans)