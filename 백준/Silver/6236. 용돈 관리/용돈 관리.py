import sys
input = sys.stdin.readline

n, m = map(int, input().split())
need = [int(input()) for _ in range(n)]



def can_withdraw(k):
    cnt = 1
    left = k
    for cost in need:
        if cost <= left:
            left -= cost
        else:
            cnt += 1
            left = k - cost
    return cnt <= m        

left = max(need)
right = sum(need)
while left <= right:
    mid = (left + right) // 2
    
    if can_withdraw(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)