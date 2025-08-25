import sys
input = sys.stdin.readline

matrix = [input().strip().split() for _ in range(10)]

eggplant10 = 0
for row in matrix:
    if len(set(row)) == 1:
        eggplant10 = 1
        break
if not eggplant10:
    for col in zip(*matrix):
        if len(set(col)) == 1:
            eggplant10 = 1
            break
            
print(eggplant10)