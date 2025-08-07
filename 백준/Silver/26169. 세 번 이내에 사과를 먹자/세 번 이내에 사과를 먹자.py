import sys
input=sys.stdin.readline

from collections import deque
import copy

board=[list(map(int, input().split())) for _ in range(5)]
r, c=map(int, input().split())



direction=[(-1,0),(1,0),(0,-1),(0,1)] # 상, 하, 좌, 우
queue=deque()
queue.append((r, c, 3, 0, board))

while queue:
    x, y, left_move, apples, cur_board=queue.popleft()

    if apples>=2:
        print(1)
        break
    if left_move==0:
        continue # 다른 경로 탐색

    for dx, dy in direction:
        nx, ny=x+dx, y+dy

        if 0 <= nx < 5 and 0 <= ny < 5 and cur_board[nx][ny] != -1:
            new_board=copy.deepcopy(cur_board)
            new_board[x][y]=-1 # 이동 전 칸 장애물로 처리
            new_apples=apples+(1 if new_board[nx][ny] == 1 else 0)
            new_board[nx][ny]=0 # 사과 먹은 칸

            queue.append((nx, ny, left_move - 1, new_apples, new_board))

else:  # 사과 2개 이상 못 먹음
    print(0)