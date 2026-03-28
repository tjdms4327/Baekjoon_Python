import sys
input = sys.stdin.readline

keyboard = [input().strip() for _ in range(4)]
memo = input().strip()

for i in range(4):
    for j in range(10):
        cnt = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < 4 and 0 <= ny < 10:
                    if keyboard[nx][ny] in memo:
                        cnt += 1
        if cnt == 9:
            print(keyboard[i][j])
            sys.exit()