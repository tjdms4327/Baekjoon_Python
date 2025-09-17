import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = [0] * m # 수열 저장 리스트
visited = [False] * n # 숫자 사용 여부 저장 리스트

def backtrack(length):
    if length == m:
        print(' '.join(str(x+1) for x in S))
        return 
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            backtrack(length+1)
            visited[i] = False # 백트래킹(수 반납)

backtrack(0)