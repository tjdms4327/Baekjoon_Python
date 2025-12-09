import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n==m==0:
        break
    
    A = [int(input()) for _ in range(n)]
    B = [int(input()) for _ in range(m)]
    
    sumA = sum(A)
    sumB = sum(B)
    best_sum = float('inf')
    answer = None
    for a in A:
        for b in B:
            newA = sumA - a + b
            newB = sumB - b + a
            
            if newA == newB:
                if a + b < best_sum:
                    best_sum = a + b
                    answer = (a, b)
    
    if answer is not None:
        print(*answer)    
    else:
        print(-1)