# bronzeII_2948
import sys
input = sys.stdin.readline

day31 = [1, 3, 5, 7, 8, 10, 12]
day_of_week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 
               4:'Friday', 5:'Saturday', 6:'Sunday'}

d, m = map(int, input().split())

day = d + 2
for month in range(1, m):
    if month == 2:
        day += 28
    elif month in day31:
        day += 31
    else:
        day += 30
day %= 7

print(day_of_week[day])