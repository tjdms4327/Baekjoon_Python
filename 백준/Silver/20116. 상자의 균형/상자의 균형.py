# silverIII_20116
import sys
input = sys.stdin.readline

n, L = map(int, input().split())
X = list(map(int, input().split()))

suffix_sum = [0]*n
suffix_sum[-1] = 0 
for i in range(n-2, -1, -1):
    suffix_sum[i] = suffix_sum[i+1] + X[i+1]

for i in range(n-1):
    total = suffix_sum[i] 
    count = n - (i+1) 
    avg = total / count
    if not (X[i]-L < avg < X[i]+L): 
        print("unstable")
        sys.exit()
print("stable")
