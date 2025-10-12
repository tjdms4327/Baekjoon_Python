# silverIV_13411
import sys
input = sys.stdin.readline

n = int(input())
time = []
for i in range(n):
    x, y, v = map(int, input().split())
    t = (x**2 + y**2)**0.5 / v
    time.append((t, i+1))
    
time.sort() # 시간 기준 정렬
for t, idx in time:
    print(idx)