# bronzeI_11383
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
picture1 = [list(input().strip()) for _ in range(n)]
picture2 = [list(input().strip()) for _ in range(n)]

for row in range(n):
    for col in range(m):
        if picture1[row][col] != picture2[row][col*2] \
        or picture1[row][col] != picture2[row][col*2+1]:
            print('Not Eyfa')
            sys.exit()
print('Eyfa')