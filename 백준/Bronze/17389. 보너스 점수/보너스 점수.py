# bronzeII_17389
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

score = 0
bonus = 0
for i in range(n):
    if s[i] == 'O':
        score += (i+1) + bonus
        bonus += 1
    else:
        bonus = 0
print(score)