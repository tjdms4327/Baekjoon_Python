import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))

m = int(input())
A = list(map(int, input().split()))
for i in A:
    if X[i-1] + 1 in X:
        continue
    else:
        if X[i-1]+1 <=2019:
            X[i-1] += 1
print(*X, sep='\n')