import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cubes = [tuple(map(int,input().split())) for _ in range(m)]

count_possible = 0
for x, y, z in cubes:
    if (x+1, y, z) in cubes and (x-1, y, z) in cubes\
        and (x, y+1, z) in cubes and (x, y-1, z) in cubes\
        and (x, y, z+1) in cubes and (x, y, z-1) in cubes:
            count_possible += 1
print(count_possible)