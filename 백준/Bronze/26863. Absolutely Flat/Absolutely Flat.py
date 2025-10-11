# bronzeIII_26863
import sys
input = sys.stdin.readline

A = [int(input()) for _ in range(4)]
b = int(input())

A.sort()
if len(set(A)) == 1 or A[0]+b == A[1] == A[2] == A[3]:
    print(1)
else:
    print(0)