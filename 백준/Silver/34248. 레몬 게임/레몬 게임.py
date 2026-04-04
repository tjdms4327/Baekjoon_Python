import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

total = sum(A)
cnt1 = A.count(1)
cnt2 = A.count(2)

if total % 3 == 0 and cnt2 <= cnt1:
    print("Yes")
else:
    print("No")