import sys
input = sys.stdin.readline

mapping = {
    'A': (0,0), 'B': (0,1), 'C': (0,2), 'D': (0,3),
    'E': (1,0), 'F': (1,1), 'G': (1,2), 'H': (1,3),
    'I': (2,0), 'J': (2,1), 'K': (2,2), 'L': (2,3),
    'M': (3,0), 'N': (3,1), 'O': (3,2)
}

matrix = [input().strip() for _ in range(4)]

result = 0
for row in range(4):
    for col in range(4):
        X = matrix[row][col]
        if X in mapping:
            x, y = mapping[X]
            result += abs(row-x) + abs(col-y)
print(result)