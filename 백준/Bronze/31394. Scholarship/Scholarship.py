import sys
input = sys.stdin.readline

n = int(input())
M = [int(input()) for _ in range(n)]

score = sum(M) / n
if all(m==5 for m in M):
    print('Named')
elif 3 in M:
    print('None')
elif score >= 4.5:
    print('High')
else:
    print('Common')