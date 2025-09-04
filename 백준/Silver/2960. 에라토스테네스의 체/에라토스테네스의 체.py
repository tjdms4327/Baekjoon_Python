import sys
input = sys.stdin.readline

n, k = map(int, input().split())
prime = [True] * (n+1)
nums = list(range(2, n+1))

for i in range(2, n+1):
    if prime[i]:
        for j in range(i, n+1, i):
            if prime[j]:
                prime[j] = False
                k -= 1
                if k == 0:
                    print(j)
                    sys.exit()