import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    while n > 2:
        if n % 2 == 1:
            count += 1
            n = n//2 + 1
        else:
            n //= 2
    print(count)