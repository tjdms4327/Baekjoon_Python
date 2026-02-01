import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))


lmin = [0]*n
lmax = [0]*n
rmin = [0]*n
rmax = [0]*n

lmin[0] = lmax[0] = A[0]
for i in range(1, n):
    lmin[i] = min(lmin[i-1], A[i])
    lmax[i] = max(lmax[i-1], A[i])

rmin[-1] = rmax[-1] = A[-1]
for i in range(n-2, -1, -1):
    rmin[i] = min(rmin[i+1], A[i])
    rmax[i] = max(rmax[i+1], A[i])


for i in range(n):
    if i == 0:
        other_min = rmin[1]
        other_max = rmax[1]
    elif i == n-1:
        other_min = lmin[n-2]
        other_max = lmax[n-2]
    else:
        other_min = min(lmin[i-1], rmin[i+1])
        other_max = max(lmax[i-1], rmax[i+1])

    print(max(abs(A[i] - other_min), abs(A[i] - other_max)))
