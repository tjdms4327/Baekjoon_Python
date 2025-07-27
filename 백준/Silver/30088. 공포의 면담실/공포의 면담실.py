import sys
input=sys.stdin.readline

n=int(input().strip())
time=[]
for _ in range(n):
    m, *t=map(int, input().strip().split())
    time.append(sum(t))
time.sort()

prefix_sum=[0]*(n+1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + time[i]
print(sum(prefix_sum))