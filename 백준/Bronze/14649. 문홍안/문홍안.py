import sys
input = sys.stdin.readline

p = int(input())

rock = [0]*(101) # 1부터 시작
n = int(input())
for _ in range(n):
    start, direction = input().strip().split()
    start = int(start)
    
    if direction == 'R':
        for i in range(start+1, 101):
            rock[i] += 1
    else:
        for i in range(start-1, 0, -1):
            rock[i] += 1
    
blue = red = green = 0
for i in range(1, 101):
    color = rock[i] % 3
    if color == 0:
        blue += 1
    elif color == 1:
        red += 1
    else:
        green += 1


print(f'{p*(blue/100):.2f}')
print(f'{p*(red/100):.2f}')
print(f'{p*(green/100):.2f}')