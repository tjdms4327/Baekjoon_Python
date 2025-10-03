# silverIII_13251
D = [0]*51
probability = [0]*51
m = int(input())
D = list(map(int, input().split()))
t = 0

for i in range(0, m):
    t += D[i]

k = int(input())
ans = 0
for i in range(0, m):
    if D[i] >= k:
        probability[i] = 1
        for j in range(0, k):
            probability[i] = probability[i] * (D[i] - j) / (t - j)
        ans += probability[i]
print(ans)