import sys
input = sys.stdin.readline

def find_q(n):
    left, right=0, 2**32
    while left<=right:
        mid=(left+right)//2
        square=mid*mid
        if square>=n:
            right=mid-1
        else: left=mid+1
    return left

n = int(input().strip())
result=find_q(n)
print(result)