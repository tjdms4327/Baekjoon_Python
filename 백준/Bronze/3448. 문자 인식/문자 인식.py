# bronzeI_3448
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    r, a = 0, 0
    
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '':
            break
        
        for char in line:
            if char != '#':
                r += 1
            a += 1
    
    ratio = round(r / a * 100, 1)

    if str(ratio).split('.')[-1] == '0':
        ratio = int(ratio)
    print(f'Efficiency ratio is {ratio}%.')
