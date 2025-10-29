# bronzeI_17072
import sys
input = sys.stdin.readline

def intensity(r, g, b):
    I = 2126*r + 7152*g + 722*b
    
    if I < 510000:
        return '#'
    elif I < 1020000:
        return 'o'
    elif I < 1530000:
        return '+'
    elif I < 2040000:
        return '-'
    else:
        return '.'

n, m = map(int, input().split())
for _ in range(n):
    line = list(map(int, input().split()))
    
    row = []
    for i in range(0, 3*m, 3):
        r, g, b = line[i:i+3]
        row.append(intensity(r, g, b))
    print(''.join(row))
    