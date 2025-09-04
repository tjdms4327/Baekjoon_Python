import sys
input = sys.stdin.readline

N = int(input())
prime = list(map(int,input().split()))
K = int(input())

answer = 0
for i in range (0,N):
    cnt = 0
    num = K
    while num > 1:
        cnt += (num // prime[i])
        num //= prime[i]
    answer += cnt
print(answer)