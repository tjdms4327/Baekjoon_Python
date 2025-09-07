import sys
input = sys.stdin.readline

W = int(input())
N = int(input())
S = [0] * (N+1)

for i in range(1, N+1):
    S[i] = S[i-1] + int(input())

for i in range(N+1):
    if i < 4:
        if S[i] > W:
            print(i-1)
            sys.exit()
    else:
        if S[i] - S[i-4] > W:
            print(i-1)
            sys.exit()
print(N)