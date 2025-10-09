# bronzeIII_13698
import sys
input = sys.stdin.readline

def ball_change(s):
    global balls
    for i in s:
        if i=='A':
            balls[0], balls[1] = balls[1], balls[0]
        elif i=='B':
            balls[0], balls[2] = balls[2], balls[0]
        elif i=='C':
            balls[0], balls[3] = balls[3], balls[0]
        elif i=='D':
            balls[1], balls[2] = balls[2], balls[1]
        elif i=='E':
            balls[1], balls[3] = balls[3], balls[1]
        elif i=='F':
            balls[2], balls[3] = balls[3], balls[2]
    return balls

s = input().strip()

balls = [1, 0, 0, 2]
result = ball_change(s)
print(balls.index(1) + 1)
print(balls.index(2) + 1)