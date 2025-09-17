import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
count = 0

cols = [False] * n # 열 충돌 체크
diag1 = [False] * (2 * n - 1) # 대각선 체크(row+col)
diag2 = [False] * (2 * n - 1) # 대각선 체크(row - col + n - 1)

def backtrack(row):
    global count
    if row == n:
        count += 1
        return 
    for col in range(n):
        if not cols[col] and not diag1[row+col] and not diag2[row-col+n-1]:
            cols[col] = diag1[row+col] = diag2[row-col+n-1] = True
            backtrack(row+1)
            cols[col] = diag1[row+col] = diag2[row-col+n-1] = False
    
backtrack(0)
print(count)