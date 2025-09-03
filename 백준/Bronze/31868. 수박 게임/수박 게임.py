import sys
input = sys.stdin.readline

n, k = map(int, input().split())
print(k//(2**(n-1)))