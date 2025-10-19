# bronzeI_10163
import sys
input = sys.stdin.readline

matrix = [[0]*1001 for _ in range(1001)]

n = int(input())
for case in range(1, 1+n):
    x, y, wide, height = map(int, input().split())
    
    for i in range(x, x + wide):
        matrix[i][y:y + height] = [case] * height


for case in range(1, n+1):
    cnt = 0
    for i in range(1001):
        cnt += matrix[i].count(case)
    print(cnt)