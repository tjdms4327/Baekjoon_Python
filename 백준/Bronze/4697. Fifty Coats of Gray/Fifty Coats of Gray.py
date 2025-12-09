import sys, math
input = sys.stdin.readline

while True:
    n, width, length, height, area, m = map(int, input().split())
    if n==width==length==height==area==m==0:
        break
    
    paint = width*length + 2 * (width * height) + 2 * (length * height)

    for _ in range(m):
        w, h = map(int, input().split())
        paint -= w*h
    print(math.ceil(n*paint/area))