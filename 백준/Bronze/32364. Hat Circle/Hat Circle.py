import sys
input = sys.stdin.readline

n = int(input())
H = [int(input()) for _ in range(n)]

count = 0
for i in range(n//2):
    if H[i] == H[i+n//2]:
        count += 2
print(count)