import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

if sum(A)%3==0 and A.count(2)<A.count(1):
    print('Yes')
else:
    print('No')