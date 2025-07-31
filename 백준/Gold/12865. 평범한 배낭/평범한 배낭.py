import sys
input=sys.stdin.readline

n, k=map(int, input().strip().split())

dp=[0]*(k+1)
for _ in range(n):
    w, v=map(int, input().strip().split())


    for i in range(k, w-1, -1): # 역순 반복 (중복 선택 방지)
        dp[i]=max(dp[i], dp[i-w]+v)
#print(dp)
print(max(dp))