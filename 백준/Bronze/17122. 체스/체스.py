import sys
input = sys.stdin.readline

def color_by_num(n):
    row = (n - 1) // 8 + 1
    col = (n - 1) % 8 + 1
    return col, row

def color_by_pos(n): # col: 1~8, row: 1~8
    col, row = color_by_num(n)
    return (col + row) % 2

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    b = int(b)
    
    x = (ord(a[0])-ord('A'))*8 + int(a[1])
    if color_by_pos(x) == color_by_pos(b):
        print('YES')
    else:
        print('NO')