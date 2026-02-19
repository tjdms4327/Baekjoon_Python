import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def solve(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    area = half * half
    
    if r < half and c < half:
        return solve(n-1, r, c)
    
    elif r < half and c >= half:
        return area + solve(n-1, r, c-half)
    
    elif r >= half and c < half:
        return 2*area + solve(n-1, r-half, c)
    
    else:
        return 3*area + solve(n-1, r-half, c-half)

print(solve(n, r, c))