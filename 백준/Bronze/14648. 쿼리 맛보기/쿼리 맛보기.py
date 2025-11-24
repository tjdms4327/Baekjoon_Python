import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nums = [0]+list(map(int, input().split()))

for _ in range(q):
    line = input().strip().split()
    
    if line[0] == '1':
        a, b = map(int, line[1:])
        print(sum(nums[a:b+1]))
        nums[a], nums[b] = nums[b], nums[a]
    else:
        a, b, c, d = map(int, line[1:])
        print(sum(nums[a:b+1]) - sum(nums[c:d+1]))