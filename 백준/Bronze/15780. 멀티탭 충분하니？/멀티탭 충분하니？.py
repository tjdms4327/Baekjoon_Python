import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))



holes = 0
for h in A:
    holes += (h // 2) + (1 if h % 2 ==1 else 0)
    
if holes >= n:
    print('YES')
else: print('NO')