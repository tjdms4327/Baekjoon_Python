import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    sorted_A = sorted(A)
    B = [0]*n
    temp = 1
    for i in range(n):
        if temp == A[i]:
            temp += 1
        B[i] = temp
        temp += 1
    print(B[-1])