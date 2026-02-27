import sys
input = sys.stdin.readline

N = int(input())
O = int(input())

solutions = []

for q in range(0, 200):  
    r = O - (N-1)*q
    if 0 <= r < N:
        T = N*q + r
        solutions.append(T)

print(min(solutions), max(solutions))