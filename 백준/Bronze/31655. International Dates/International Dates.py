import sys
input = sys.stdin.readline

date = list(map(int, input().strip().split('/')))
if date[0] > 12 and date[1] <= 12:
    print('EU')
elif date[1] > 12 and date[0] <= 12:
    print('US')
else:
    print('either')