import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

common = set()
for a in set(A):
    if a in B:
        common.add(a)

for x in sorted(common):
    print(x)