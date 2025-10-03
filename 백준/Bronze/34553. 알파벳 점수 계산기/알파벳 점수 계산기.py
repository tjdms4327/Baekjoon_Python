# bronzeIII_34552
import sys
input = sys.stdin.readline

s = input().strip()

temp = 1
score = temp
for i in range(1, len(s)):
    if s[i-1] < s[i]:
        temp += 1
    else:
        temp = 1
    score += temp
print(score)