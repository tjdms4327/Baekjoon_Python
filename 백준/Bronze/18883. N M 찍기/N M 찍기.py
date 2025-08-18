n, m = map(int, input().split())

nums=list(range(1, n*m+1))
for i in range(0, n*m, m):
    slice = nums[i:i+m]
    print(*slice)