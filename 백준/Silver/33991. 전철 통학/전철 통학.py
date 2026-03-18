import sys
input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())
q = int(input())

for _ in range(q):
    x, y, t1, t2, t3 = map(int, input().split())
    
    d1 = abs(x-x1) + abs(y-y1)
    d2 = abs(x-x2) + abs(y-y2)
    d3 = abs(x-x3) + abs(y-y3)
    
    time1 = d1 + (t1 - d1 % t1) % t1
    time2 = d2 + (t2 - d2 % t2) % t2
    time3 = d3 + (t3 - d3 % t3) % t3
    
    print(min(time1, time2, time3))