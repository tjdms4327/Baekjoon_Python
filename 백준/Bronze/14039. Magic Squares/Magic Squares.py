import sys
input = sys.stdin.readline

M = [list(map(int, input().split())) for _ in range(4)]

sum_rc = []
for row in M:
    if sum_rc:
        if sum_rc[-1] != sum(row):
            print('not magic')
            sys.exit()
    else:
        sum_rc.append(sum(row))
for c in zip(*M):
    col_sum = sum(list(c))
    if col_sum != sum_rc[-1]:
        print('not magic')
        sys.exit()
print('magic')