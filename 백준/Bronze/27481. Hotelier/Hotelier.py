import sys
input = sys.stdin.readline

n = int(input())
s = list(input().strip())

room = [0]*10
for x in s:
    if x.isdigit():
        room[int(x)] = 0
    elif x == 'L':
        idx = room.index(0)
        room[idx] = 1
    elif x == 'R':
        temp = room[::-1].index(0)
        idx = 9 - temp
        room[idx] = 1
print(*room, sep='')