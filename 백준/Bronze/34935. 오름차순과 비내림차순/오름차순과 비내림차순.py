import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

if sorted(A)==A and len(set(A))==n:
    print(1)
else:
    print(0)