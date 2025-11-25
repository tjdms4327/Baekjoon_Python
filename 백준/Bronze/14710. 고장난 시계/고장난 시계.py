import sys
input = sys.stdin.readline

angle1, angle2 = map(int, input().split())


if angle2 % 6 != 0:
    print('X')
    sys.exit()

m = angle2 // 6
ok = False
for h in range(12):
    if abs(angle1 - (30*h + 0.5*m)) < 1e-9:
        ok = True
        break
print('O' if ok else 'X')