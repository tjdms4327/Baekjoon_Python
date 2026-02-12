import sys
input = sys.stdin.readline

n, _ = map(int, input().split())
K = list(map(int, input().split()))

answer = 0

def dfs(num):
    global answer
    
    if num > n:
        return
    
    if num != 0:
        answer = max(answer, num)
    
    for k in K:
        dfs(num * 10 + k)

dfs(0)
print(answer)
