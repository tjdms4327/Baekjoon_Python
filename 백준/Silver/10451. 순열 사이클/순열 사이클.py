import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n=int(input())
    permutation=list(map(int, input().split()))

    visited=[False]*n
    cnt=0
    for i in range(n):
        if not visited[i]:
            cnt+=1
            cur=i
            while not visited[cur]:
                visited[cur]=True
                cur=permutation[cur]-1 # 인덱스 맞추기
    print(cnt)