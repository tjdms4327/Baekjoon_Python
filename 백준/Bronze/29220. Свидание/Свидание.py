# bronzeIII_29220
import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
A = list(map(int, input().split()))

A.sort()
if sum(A[1:]) < k:
    print('NO')
else:
    print('YES')