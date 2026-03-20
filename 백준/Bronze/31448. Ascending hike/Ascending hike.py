import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

height = [A[0], A[0]]
best = 0
for i in range(1, n):
    if A[i] <= A[i-1]:
        best = max(best, height[-1]-height[0])
        height[0] = A[i]
        
    height[-1] = A[i]
    
best = max(best, height[-1]-height[0])
print(best)