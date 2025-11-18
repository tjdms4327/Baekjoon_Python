# bronzeI_25425
import sys, math
input = sys.stdin.readline

n, m, a, k = map(int, input().split())

Max = min(a-k, n-1) + 1
Min = max(1, math.ceil((a-k)/m)+1)
print(Max, Min)