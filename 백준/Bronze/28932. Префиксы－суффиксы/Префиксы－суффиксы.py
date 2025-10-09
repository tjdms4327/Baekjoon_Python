# bronzeIII_28932
import sys
input = sys.stdin.readline

n = int(input())
A = list(input().split())

for i in range(n):
    for j in range(n):
        s1, s2 = A[i], A[j]
        for k in range(1, len(s1)+1):
            prefix = s1[:k]
            if s2.endswith(prefix):
                print(i+1, j+1)
                exit()
print(-1)