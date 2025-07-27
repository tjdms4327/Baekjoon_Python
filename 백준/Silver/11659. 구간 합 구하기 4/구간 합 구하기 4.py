import sys
input=sys.stdin.readline

n,m=map(int, input().split())
nums=list(map(int, input().split()))



# 누적합 배열
prefix_sum=[0]
for i in nums:
    prefix_sum.append(prefix_sum[-1]+i)
# 구간 합
def range_sum(left, right):
    print(prefix_sum[right]-prefix_sum[left-1])
    return 0

for _ in range(m):
    i, j=map(int, input().split())
    range_sum(i,j)