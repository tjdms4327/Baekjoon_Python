# bronzeIII_21614.py
import sys
input = sys.stdin.readline

past_direction = ''
while True:  
    n = input().strip()
    if n == '99999': break
    
    digit0, digit1 = int(n[0]), int(n[1])
    sum_01 = digit0 + digit1
    if sum_01 == 0:
        print(past_direction, n[2:])
    elif (digit0 + digit1) % 2 == 1:
        print('left', n[2:])
        past_direction = 'left'
    else:
        print('right', n[2:])
        past_direction = 'right'