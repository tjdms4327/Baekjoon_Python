import sys
input=sys.stdin.readline

n=int(input())
M=list(map(int, input().split()))

prefix_sum=[0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i]=prefix_sum[i-1]+M[i-1]



k=int(input())
delivery=[]
for _ in range(k):
    a, t=map(int, input().split())
    time=prefix_sum[a] # 창고에서 a까지
    if time>t:
        print(-1)
        sys.exit()
    delivery.append(a)
max_city=max(delivery)
print(prefix_sum[max_city]*2)