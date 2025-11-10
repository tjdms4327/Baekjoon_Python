# bronzeII_27522
import sys
input = sys.stdin.readline

rank = []
for _ in range(8):
    time, team = input().strip().split()
    M, SS, sss = map(int, time.split(':'))
    t = sss + SS*1000 + M*1000*60
    rank.append([team, t])
rank.sort(key = lambda x:x[1])

score = [10, 8, 6, 5, 4, 3, 2, 1]
red = 0
for i in range(8):
    team = rank[i][0]
    if team == 'R':
        red += score[i]
blue = sum(score) - red

if red > blue:
    print('Red')
else:
    print('Blue')