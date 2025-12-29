import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

p = sum(A)
for b in B:
    if b != 0:
        p *= b
print(p)