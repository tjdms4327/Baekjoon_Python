# bonzeI_18125
import sys
input = sys.stdin.readline

r, c= map(int, input().split())

matrix = [list(input().strip().split()) for _ in range(c)]
real_matrix = []
for col in zip(*matrix):
    real_matrix.append(list(reversed(col)))

give = [list(input().strip().split()) for _ in range(r)]
for r in range(r):
    if real_matrix[r] != give[r]:
        print('''|>___/|     /}
| O O |    / }
( =0= )\"\"\"\"  \\
| ^  ____    |
|_|_/    ||__|''')
        sys.exit()
print('''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|''')