# bronzeII_31844
import sys
input = sys.stdin.readline

storage = list(input().strip())

robot_pos = storage.index('@')
box_pos = storage.index('#')
want_pos = storage.index('!')

if robot_pos <= box_pos <= want_pos \
    or robot_pos >= box_pos >= want_pos:
        print(abs(robot_pos - want_pos) - 1)
else:
    print(-1)