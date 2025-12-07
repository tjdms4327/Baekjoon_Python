import sys
input = sys.stdin.readline

while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break
    
    K = list(map(int, input().split()))
    tot = n
    for i in range(m-1):
        n += K[i%k]
        tot += n
    print(tot)