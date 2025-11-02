# bronzeII_25576
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
L = list(map(int, input().split()))

bad_count = 0
for _ in range(n-1):
    K = list(map(int, input().split()))
    diff = sum(abs(K[i] - L[i]) for i in range(m))
    
    if diff > 2000:
        bad_count += 1

if bad_count >= (n-1)/2:
    print('YES')
else:
    print('NO')