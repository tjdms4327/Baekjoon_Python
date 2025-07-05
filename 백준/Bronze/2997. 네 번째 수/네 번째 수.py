nums=list(map(int, input().split()))
nums.sort()

d=nums[1]-nums[0]
k=nums[2]-nums[1]
if k==d:
    x=nums[-1]+d
else:
    if d>k:
        x=nums[0]+k
    else:
        x=nums[1]+d
print(x)