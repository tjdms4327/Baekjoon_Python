import sys
input = sys.stdin.readline

A, B = map(int, input().split())
if B > 0:
    print(A//B)
    print(A%B)
else:
    print(-(A//-B))
    print(A%-B)