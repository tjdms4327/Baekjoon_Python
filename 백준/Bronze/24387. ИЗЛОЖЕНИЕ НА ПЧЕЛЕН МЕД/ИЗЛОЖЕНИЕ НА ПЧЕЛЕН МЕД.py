# bronzeIII_24387
import sys
input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(); B.sort()
print(sum(A[i]*B[i] for i in range(3)))