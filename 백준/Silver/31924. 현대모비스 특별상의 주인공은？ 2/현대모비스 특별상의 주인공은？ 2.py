import sys
input = sys.stdin.readline

n = int(input())
board = [input().strip() for _ in range(n)]


dirs = [
    (0,1), (0,-1),
    (1,0), (-1,0),
    (1,1), (1,-1),
    (-1,1), (-1,-1)
]

target = "MOBIS"
count = 0
for r in range(n):
    for c in range(n):
        for dr, dc in dirs:
            found = True
            for k in range(5):
                nr = r + dr*k
                nc = c + dc*k
                
                if not (0 <= nr < n and 0 <= nc < n):
                    found = False
                    break
                if board[nr][nc] != target[k]:
                    found = False
                    break
            
            if found:
                count += 1

print(count)
