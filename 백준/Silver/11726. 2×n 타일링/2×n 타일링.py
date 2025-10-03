# silverIII_11726
mod = 10007
n = int(input())
D = [0] * 1001
D[1] = 1
D[2] = 2

for i in range(3, n+1):
    D[i] = (D[i-1] + D[i-2]) % mod
print(D[n])