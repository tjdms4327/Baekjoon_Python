# bronzeII_14697
import sys
input = sys.stdin.readline

a, b, c, n = map(int, input().split())

for room1 in range(n//a+1):
    for room2 in range(n//b+1):
        for room3 in range(n//c+1):
            if room1*a + room2*b + room3*c == n:
                print(1)
                exit()
print(0)