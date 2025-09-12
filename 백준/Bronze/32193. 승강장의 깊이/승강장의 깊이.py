import sys
input = sys.stdin.readline

n = int(input())
A, B = [0], [0]
for _ in range(n):
    a, b = map(int, input().split())
    A.append(A[-1] + a)
    B.append(B[-1] + b)
    
    print(A[-1] - B[-1])