# bronzeII_1592
import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

ball_count = [0] * (n+1)
index = 1
while m not in ball_count:
    ball_count[index] += 1
    if ball_count[index] % 2 == 1:
        index = (index+l - 1) % n + 1
    else:
        index = (index-l - 1) % n + 1
print(sum(ball_count) - 1)