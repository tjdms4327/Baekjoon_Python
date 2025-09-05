import sys
input = sys.stdin.readline

n = int(input())
score = 0
while n != 1:
    score += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
print(score)