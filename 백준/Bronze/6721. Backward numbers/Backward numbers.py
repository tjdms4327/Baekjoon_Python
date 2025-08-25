import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    tot = int(a[::-1]) + int(b[::-1])
    print(int(str(tot)[::-1]))