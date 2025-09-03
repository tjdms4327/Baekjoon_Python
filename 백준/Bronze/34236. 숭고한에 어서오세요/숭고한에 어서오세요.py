import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
print(A[-1]*2 - A[-2])