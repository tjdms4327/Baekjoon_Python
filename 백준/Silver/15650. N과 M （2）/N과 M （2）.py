import sys
input=sys.stdin.readline

def backtrack(start):
    if len(result)==m: 
        print(' '.join(map(str, result)))
        return 
    for i in range(start, n+1): # 오름차순 유지
        result.append(i)
        backtrack(i+1)
        result.pop()
    

n, m=map(int, input().strip().split())
result=[]
backtrack(1)