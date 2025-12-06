import sys
input = sys.stdin.readline

score = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}

n = int(input())

temp = 0.0
bonus = 0.0
for _ in range(n):
    s = input().strip()
    x, y = s[0], int(s[1])
    
    temp += score[x]
    if x in "ABC":
        if y == 1:
            bonus += 0.05
        elif y == 2:
            bonus += 0.025
print(temp/n + bonus)