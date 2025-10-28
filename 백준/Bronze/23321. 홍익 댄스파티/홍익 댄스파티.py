# bronzeI_23321
import sys
input = sys.stdin.readline

dance = [['.', 'o', 'm', 'l', 'n'], 
         ['o', 'w', 'l', 'n', '.'],
         ['.', '.', 'o', 'L', 'n']]

start = [list(input().strip()) for _ in range(5)]

result = [[] for _ in range(5)]
for col in zip(*start):
    col = list(col)
    if col == dance[2]:
        for i in range(5):
            result[i].append(col[i])
    elif col == dance[0]:
        for i in range(5):
            result[i].append(dance[1][i])
    else:
        for i in range(5):
            result[i].append(dance[0][i])

for row in result:
    print(''.join(row))