N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

chess1 = ['WBWBWBWB', 'BWBWBWBW'] * 4  # 맨 위가 W로 시작하는 체스판
chess2 = ['BWBWBWBW', 'WBWBWBWB'] * 4  # 맨 위가 B로 시작하는 체스판

def count_repaints(x, y):
    cnt1, cnt2 = 0, 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess1[i][j]:
                cnt1 += 1
            if board[x + i][y + j] != chess2[i][j]:
                cnt2 += 1  
    return min(cnt1, cnt2) 

min_repaints = float('inf')

for i in range(N - 7): 
    for j in range(M - 7): 
        min_repaints = min(min_repaints, count_repaints(i, j))
print(min_repaints)
