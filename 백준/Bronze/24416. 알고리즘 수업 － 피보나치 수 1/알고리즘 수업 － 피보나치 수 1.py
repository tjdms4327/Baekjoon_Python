# bronzeI_24416
import sys
input = sys.stdin.readline

n = int(input())

f = [0, 1, 1]
for i in range(3, n + 1):
    f.append(f[i-1] + f[i-2])

print(f[n], n - 2)