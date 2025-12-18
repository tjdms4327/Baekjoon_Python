import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    A = sorted(list(map(int, input().split())))

    max_len = 0
    cur = 1
    for i in range(1, n):
        if abs(A[i-1] - A[i]) == 1:
            cur += 1
        else:
            max_len = max(max_len, cur)
            cur = 1
    max_len = max(max_len, cur)
    print(max_len)