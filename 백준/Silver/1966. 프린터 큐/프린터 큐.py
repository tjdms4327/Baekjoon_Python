from collections import deque

t=int(input())
for _ in range(t):
    n, want=map(int, input().split())
    priority=list(map(int, input().split()))

    queue=deque((i, p) for i, p in enumerate(priority))
    cnt=0 # 인쇄 순서

    while queue:
        current=queue.popleft()
        if any (current[1]<other[1] for other in queue): # 큐에 더 높은 중요도 존재
            queue.append(current) # 맨 뒤에 추가
        else:
            cnt+=1 # 인쇄
            if current[0]==want:
                print(cnt)
                break
    
    