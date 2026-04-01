import sys
input=sys.stdin.readline

def sum(a,b):
    return (b*(b+1))//2 - ((a-1)*a)//2

nums=list(map(int, input().split()))
nums.sort()
result=sum(nums[0],nums[-1])
print(result)