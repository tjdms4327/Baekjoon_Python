import sys
input = sys.stdin.readline

def diff(tuple1, tuple2):
    r0, g0, b0 = tuple1
    r1, g1, b1 = tuple2
    return (r0-r1)**2 + (g0-g1)**2 + (b0-b1)**2

k = int(input())
for case in range(1, k+1):
    n = int(input())
    rgb = [tuple(map(int, input().split())) for _ in range(n)]
    
    result = []
    best = 0
    for x in range(n):
        for y in range(x+1, n):
            diff_square = diff(rgb[x], rgb[y])
            if best == diff_square:
                result.append((x+1, y+1))
            elif best < diff_square:
                best = diff_square
                result = [(x+1, y+1)]
    
    print(f'Data Set {case}:')
    for x, y in result:
        print(x, y)
    