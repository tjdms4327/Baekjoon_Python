import sys
input = sys.stdin.readline

g, s, c = map(int, input().split())
power = 3*g + 2*s + c

if power >= 8:
    print('Province or ', end='')
elif power >= 5:
    print('Duchy or ', end='')
elif power >= 2:
    print('Estate or ', end='')
if power >= 6:
    print('Gold')
elif power >= 3:
    print('Silver')
else:
    print('Copper')