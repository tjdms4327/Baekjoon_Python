import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

down = False
for i in range(1,n):
    if A[i-1] == A[i]:
        print('NO')
        sys.exit()
        
    elif A[i-1] < A[i]:
        if down:
            print('NO')
            sys.exit()
    else:
        down = True

print('YES')