n=int(input())
B_nums=list(map(int, input().split()))

A_nums=[B_nums[0]]
for i in range(1,n):
    B_nums[i]*=(i+1)
    A_nums.append(B_nums[i]-sum(A_nums))
print(*A_nums, sep=' ')