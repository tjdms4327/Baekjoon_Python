import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

diff = A - B
length = len(diff)

print(length)
if length:
    print(*sorted(diff))