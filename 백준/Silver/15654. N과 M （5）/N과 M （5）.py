import sys
input=sys.stdin.readline

def backtrack():
    if len(result)==m: 
        print(' '.join(map(str, result)))
        return 
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            result.append(nums[i])
            backtrack()
            result.pop()
            visited[i]=False
    

n, m=map(int, input().strip().split())
nums=list(map(int, input().strip().split()))
nums.sort()
result=[]
visited=[False]*n
backtrack()