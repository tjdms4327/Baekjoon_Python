# goldV_1722
import sys
input = sys.stdin.readline

F = [0]*21
S = [0]*21
visited = [False]*21
n = int(input())
F[0] = 1
for i in range(1, n+1):
    F[i] = F[i-1]*i # 각 자릿수에서 만들 수 있는 경우의수
    
inputList = list(map(int, input().split()))
if inputList[0] == 1:
    k = inputList[1]
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:
                continue
            if k <= cnt * F[n-i]:
                k -= (cnt-1)*F[n-i]
                S[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n+1):
        print(S[i], end=' ')
else:
    k = 1
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * F[n-i]
        visited[inputList[i]] = True
    print(k)