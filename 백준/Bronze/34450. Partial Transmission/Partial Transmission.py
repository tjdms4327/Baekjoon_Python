import sys
input = sys.stdin.readline

n = int(input())
p = int(input())
S = list(map(int, input().split()))

missing = set(range(p, p+n)) - set(S)
print(*missing)