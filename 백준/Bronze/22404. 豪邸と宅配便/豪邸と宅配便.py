import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
A = [0] + list(map(int, input().split()))


time = [A[i] - A[i-1] for i in range(1, n+1)]
tot = max(0, time[0] - m)
for a in time[1:]:
    tot += max(0, a-2*m)
print(tot + max(0, t-A[n]-m))
