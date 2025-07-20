n,k=map(int, input().split())

from collections import deque
def josephus(n, k):
    q=deque(range(1, n+1))
    result=[]

    while q:
        q.rotate(-(k-1)) # k-1만큼 왼쪽으로 이동 -> 맨 앞 사람이 k번째 사람
        result.append(q.popleft())
    return result

res=josephus(n, k)
print("<" + ", ".join(map(str, res)) + ">")