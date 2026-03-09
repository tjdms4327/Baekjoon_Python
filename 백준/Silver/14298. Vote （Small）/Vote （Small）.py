import sys, math
input = sys.stdin.readline

def dfs(a, b):
    if b >= a:
        return 0
    if a > n or b > m:
        return 0
    if a == n and b == m:
        return 1
    
    return dfs(a+1, b) + dfs(a, b+1)

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    
    good = dfs(1,0)
    total = math.factorial(n+m) / (math.factorial(n)*math.factorial(m))
    
    prob = good / total
    
    print(f'Case #{case}: {prob:.8f}')