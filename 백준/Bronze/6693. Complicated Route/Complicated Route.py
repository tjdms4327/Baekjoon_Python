import sys, re
input = sys.stdin.readline

while True:   
    line = input().strip().split(',')
    if line == ['END']:
        break
    
    x, y = 0, 0
    for s in line:
        num = int(re.findall(r'\d+', s)[0])
        dir = re.findall(r'[A-Z]+', s)[0]
        
        if dir == 'N':
            y += num
        elif dir == 'S':
            y -= num
        elif dir == 'E':
            x += num
        elif dir == 'W':
            x -= num
        else:
            num = num / (2 ** 0.5)
            if 'N' in dir:
                y += num
            if 'S' in dir:
                y -= num
            if 'E' in dir:
                x += num
            if 'W' in dir:
                x -= num
    print(f'You can go to ({x:.3f},{y:.3f}), the distance is {(x**2+y**2)**0.5:.3f} steps.')