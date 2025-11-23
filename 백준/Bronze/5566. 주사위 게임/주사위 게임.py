import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] + [int(input()) for _ in range(n)]

pos = 1
count = 0
for _ in range(m):
    x = int(input())
    
    count += 1
    pos += x
    if pos >= n:
        break

    pos += board[pos]
    if pos >= n:
        break

print(count)