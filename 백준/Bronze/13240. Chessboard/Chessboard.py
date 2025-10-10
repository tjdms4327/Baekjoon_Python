# bronzeIII_13240
import sys
input = sys.stdin.readline

m , n = map(int, input().split())

matrix = [list('*.*.*.*.*.'), list('.*.*.*.*.*')]
for i in range(m):
    print(''.join(matrix[i%2][:n]))