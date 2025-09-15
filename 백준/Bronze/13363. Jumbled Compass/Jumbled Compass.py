import sys
input = sys.stdin.readline

n1 = int(input())
n2 = int(input())

cw = (n2 - n1) % 360 # 시계방향
ccw = (n1 - n2) % 360 # 반시계방향
if cw <= ccw:
    print(cw if cw != 180 else 180)  # 180이면 시계방향
else:
    print(-ccw)