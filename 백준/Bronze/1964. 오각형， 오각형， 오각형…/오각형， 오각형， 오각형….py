# bronzeII_1964
import sys
input = sys.stdin.readline

n = int(input())

spot = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        spot[i] = 5
    else:
        spot[i] = 1 + 3*i
print(sum(spot) % 45678)