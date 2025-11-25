import sys
input = sys.stdin.readline

n = int(input())
book = [0] * 32
for _ in range(n):
    s, e = map(int, input().split())
    for i in range(s, e):
        book[i] += 1

k = int(input())
if any(i for i in book if i>k):
    print(0)
else:
    print(1)