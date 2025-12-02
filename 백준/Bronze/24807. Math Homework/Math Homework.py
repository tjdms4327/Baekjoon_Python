import sys
input = sys.stdin.readline

b, d, c, l = map(int, input().split())

res = []
for x in range(l//b + 1):
    for y in range(l//d + 1):
        reminder = l - b*x - d*y
        if reminder >= 0 and reminder % c == 0:
            res.append((x, y, reminder//c))

if res:
    for i in res:
        print(*i)
else:
    print('impossible')
