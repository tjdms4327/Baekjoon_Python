import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
u, d = map(int, input().split())

cnt1 = A.count(1)
cnt2 = A.count(2)
cnt3 = A.count(3)

if cnt1 > u or cnt2 > d or cnt1 + cnt3 < u or cnt2 + cnt3 < d:
    print("NO")
    sys.exit()

res = [''] * n
for i in range(n):
    if A[i] == 1:
        res[i] = 'U'
        u -= 1
    elif A[i] == 2:
        res[i] = 'D'

for i in range(n):
    if A[i] == 3:
        if u > 0:
            res[i] = 'U'
            u -= 1
        else:
            res[i] = 'D'

print("YES")
print(''.join(res))
