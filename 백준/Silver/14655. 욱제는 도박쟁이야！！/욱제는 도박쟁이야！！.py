import sys
input = sys.stdin.readline

n = int(input())
round1 = list(map(int, input().split()))
round2 = list(map(int, input().split()))

S = sum(abs(x) for x in round1)
print(2 * S)
