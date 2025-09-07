import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

v = 0
for a in A:
    v = 1 - (1-v)*(1-a/100.0)
    print(v*100)