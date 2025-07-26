import sys
input=sys.stdin.readline

def backtrack(start):
    if len(result)==m: 
        print(' '.join(map(str, result)))
        return 

    prev=0
    for i in range(start, n):
        if nums[i]!=prev:
            result.append(nums[i])
            prev=nums[i] # 같은 depth에서 같은 값은 한 번만 사용
            backtrack(i)
            result.pop()
    

n, m=map(int, input().strip().split())
nums=list(map(int, input().strip().split()))
nums.sort()
result=[]
backtrack(0)