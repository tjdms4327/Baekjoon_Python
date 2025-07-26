import sys
input=sys.stdin.readline

def backtrack():
    if len(result)==m: 
        print(' '.join(map(str, result)))
        return 

    prev=0 # 이번 depth에서 직전에 쓴 숫자
    for i in range(n):
        if not visited[i] and nums[i]!=prev:
            visited[i]=True
            result.append(nums[i])
            prev=nums[i] # 이번 depth에서 이 숫자는 다시 사용X
            backtrack()
            result.pop()
            visited[i]=False
    

n, m=map(int, input().strip().split())
nums=list(map(int, input().strip().split()))
nums.sort()
result=[]
visited=[False]*n
backtrack()