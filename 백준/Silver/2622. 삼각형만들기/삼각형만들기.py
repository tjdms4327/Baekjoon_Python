import sys
input = sys.stdin.readline

t = int(input())

count = 0
for a in range(1, t):
    for b in range(a, t):
        c = t - a - b
        if (a<=b<=c) and a+b > c:
            count += 1
print(count)