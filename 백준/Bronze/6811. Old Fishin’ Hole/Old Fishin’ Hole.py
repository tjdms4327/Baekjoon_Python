import sys
input = sys.stdin.readline

brown = int(input())
north = int(input())
yellow = int(input())
score = int(input())

count = 0
for b in range(score//brown+1):
    for n in range((score-b*brown)//north+1):
        for y in range((score-b*brown-n*north)//yellow+1):
            if (score >= b*brown + n*north + y*yellow) and (b>0 or n>0 or y>0):
                count += 1
                print(f'{b} Brown Trout, {n} Northern Pike, {y} Yellow Pickerel')
print(f'Number of ways to catch fish: {count}')