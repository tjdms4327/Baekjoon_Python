# bronzeI_10163
import sys
input = sys.stdin.readline

matrix = [[0]*1001 for _ in range(1001)]

n = int(input())
for case in range(1, 1+n):
    x, y, wide, height = map(int, input().split())
    
    for row in range(x, x+wide):
        for col in range(y , y+height):
            matrix[row][col] = case


for case in range(1, n+1):
    count = 0
    for i in range(1001):
        count += matrix[i].count(case)
    print(count)