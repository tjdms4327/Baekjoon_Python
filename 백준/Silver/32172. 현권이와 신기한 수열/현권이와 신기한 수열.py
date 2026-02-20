import sys
input = sys.stdin.readline

n = int(input())
A = [0]
for i in range(1, n+1):
    a = A[-1] - i
    if a < 0 or a in A:
        a = A[-1] + i
        
    A.append(a)
    
print(A[-1])