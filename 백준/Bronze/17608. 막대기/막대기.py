import sys
input = sys.stdin.readline

n=int(input())
lobs=[int(input()) for _ in range(n)]

last = lobs[-1]
count = 1
for i in reversed(range(n)):
    if lobs[i] > last:
        count += 1
        last = lobs[i]
print(count)