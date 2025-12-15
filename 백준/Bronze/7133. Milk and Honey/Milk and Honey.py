import sys
input = sys.stdin.readline

m, d1 = map(int, input().split())
h, d2 = map(int, input().split())

n = int(input())
tot = 0
for _ in range(n):
    c, b = map(int, input().split())
    
    happy_c = sum(m - i*d1 for i in range(c) if m - i*d1 > 0)
    happy_b = sum(h - i*d2 for i in range(b) if h - i*d2 > 0)
    tot += max(happy_b, happy_c)
print(tot)