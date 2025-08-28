import sys
input = sys.stdin.readline

n = int(input())
ocean, temp, oxygen = 0, -30, 0
for _ in range(n):
    s, t = input().strip().split()
    t  = int(t)

    if s == 'ocean':
        ocean += t
    elif s == 'oxygen':
        oxygen += t
    elif s =='temperature':
        temp += t

if (ocean >= 9) and (temp >= 8) and (oxygen >= 14):
    print('liveable')
else:
    print('not liveable')