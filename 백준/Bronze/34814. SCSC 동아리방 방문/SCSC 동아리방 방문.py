import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

for _ in range(m):
    like, hate = map(int, input().split())
    
    max_idx = A.index(max(A))
    if max_idx == hate or len(set(A[1:]))==1:
        continue
    else:
        A[like] -= 1

print(*A[1:])