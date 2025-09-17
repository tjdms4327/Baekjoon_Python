import sys
input = sys.stdin.readline

n = int(input())
x = [int(input()) for _ in range(n)]

energy = 0
for i in range(n-1):
    energy += (x[i+1] - x[i]) ** 2
print(energy)