import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

penguin = A.index(-1)
left = A[:penguin]
right = A[penguin+1:]
print(min(left) + min(right))