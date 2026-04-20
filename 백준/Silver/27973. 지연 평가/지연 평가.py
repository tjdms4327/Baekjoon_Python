import sys
input = sys.stdin.readline

start = 1
mul = 1
add = 0

q = int(input())
for _ in range(q):
    line = input().strip()
    if line[0] == '3':
        print(start*mul + add)
    else:
        command, x = map(int, line.split())
        if command == 0:
            add += x
        elif command == 2:
            start += x
        elif command == 1:
            mul *= x
            add *= x