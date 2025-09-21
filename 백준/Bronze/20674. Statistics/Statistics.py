# bronzeIII_20674
n = int(input())
pi = [int(input()) for _ in range(n)]

total = 0
min_pi = float('inf')
for i in range(n):
    if pi[i] < min_pi:
        min_pi = pi[i]
    else:
        total += pi[i] - min_pi
print(total)