import sys
input = sys.stdin.readline

n = int(input())
T, S = [0] * n, [0] * n
for i in range(n):
    ti, si = map(int, input().split())
    T[i] += ti
    S[i] += si
    
idx_sk = S.index(max(S))
if S[idx_sk] == 0:
    penalty = 0
elif S[idx_sk] in [1, 4]:
    penalty = T[idx_sk] + (idx_sk) * 20
print(penalty)