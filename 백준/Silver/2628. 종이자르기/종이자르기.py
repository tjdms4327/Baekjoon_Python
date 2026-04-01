import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())

hor_cut = [0, h]
ver_cut = [0, w]
for _ in range(n):
    dir, pos = map(int, input().split())
    if dir == 0:
        hor_cut.append(pos) 
    else:
        ver_cut.append(pos)  

hor_cut.sort()
ver_cut.sort()


max_area = 0
for i in range(1, len(hor_cut)):
    for j in range(1, len(ver_cut)):
        height = hor_cut[i] - hor_cut[i-1]
        width = ver_cut[j] - ver_cut[j-1]
        max_area = max(max_area, height * width)

print(max_area)