# bronzeI_2804
import sys
input = sys.stdin.readline

A, B = input().strip().split()

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            ai, bj = i, j
            break
    else:
        continue
    break

for y in range(len(B)):
    if y == bj:
        print(A)
    else:
        print('.' * ai + B[y] + '.' * (len(A) - ai - 1))
