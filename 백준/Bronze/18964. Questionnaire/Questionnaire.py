# bronzeIII_18964
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for m in range(1, max(A)+1):
    for k in range(m):
        count = 0
        if sum(1 for a in A if a%m == k) >= n//2+1:
            print(m, k)
            exit()
            