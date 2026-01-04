import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

ok = True
for i in range(1, n-1):
    if A[i-1] + A[i+1] != 2*A[i]:
        ok = False
        break
if ok:
    print('YES')
else:
    print('NO')
    sys.exit()
    
B, C = [], []
for x in A:
    B.append(x*2)
    C.append(-x)
print(*B)
print(*C)