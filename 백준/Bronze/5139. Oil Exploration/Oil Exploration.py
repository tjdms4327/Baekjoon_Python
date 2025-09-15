import sys
input = sys.stdin.readline

for case in range(1, int(input())+1):
    print(f'Data Set {case}:')
    h, w = map(int, input().split())
    s = [input().strip() for _ in range(h)]
    result = []
    for col in zip(*s):
        col = list(col)
        if 'X' not in col:
            result.append('N')
        else:
            idx_x = col.index('X')
            result.append(str(3 * col[:idx_x].count('H') + col[:idx_x].count('S')))
    print(' '.join(result))
    print()