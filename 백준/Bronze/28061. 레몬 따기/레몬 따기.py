import sys 
input = sys.stdin.readline

n = int(input())
lemons = list(map(int, input().split()))

for i in range(n):
    lemons[i] -= (n-i)
print(max(lemons))