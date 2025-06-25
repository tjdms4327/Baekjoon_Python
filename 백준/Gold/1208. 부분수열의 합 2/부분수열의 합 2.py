from collections import defaultdict
import sys
input=sys.stdin.readline

N,S=map(int, input().split())
nums=list(map(int, input().split()))

cnt=0
summ_dict=defaultdict(int)
def right_search(mid, partial_sum):
    if mid==N:
        summ_dict[partial_sum]+=1
        return
    right_search(mid+1, partial_sum)
    right_search(mid+1, partial_sum+nums[mid])
def left_search(st, partial_sum):
    global cnt
    if st==N//2:
        if summ_dict[S-partial_sum]:
            cnt+=summ_dict[S-partial_sum]
        return 
    left_search(st+1, partial_sum)
    left_search(st+1, partial_sum+nums[st])

right_search(N//2, 0)
left_search(0,0)
print(cnt if S else cnt-1)