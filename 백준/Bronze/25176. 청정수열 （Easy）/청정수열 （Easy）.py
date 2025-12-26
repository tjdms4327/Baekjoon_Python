import sys
input = sys.stdin.readline

n = int(input())

tot = 1
for i in range(2, n+1):
    tot *= i
print(tot)