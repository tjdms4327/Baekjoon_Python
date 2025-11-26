import sys
input = sys.stdin.readline

mapping = {1:1, 8:8, 2:5, 5:2,
           3:'?', 4:'?', 6:'?', 7:'?', 9:'?'}

w, n = input().strip().split()
n = int(n)

matrix = [list(map(int, input().split())) for _ in range(n)]
if w in 'LR':
    for row in matrix:
        r = [mapping[i] for i in row[::-1]]
        print(*r)
else:
    m = matrix[::-1]
    for row in m:
        r =  [mapping[i] for i in row]
        print(*r)
