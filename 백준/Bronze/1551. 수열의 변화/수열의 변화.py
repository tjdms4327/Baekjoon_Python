# bronzeI_1551
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split(',')))

for _ in range(k):
    A = [A[i+1] - A[i] for i in range(len(A)-1)]
print(*A, sep=',')