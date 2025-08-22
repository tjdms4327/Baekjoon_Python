import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))


past = nums[0]
scores = [past]
for i in nums[1:]:
    if i == (past + 1):
        pass
    else:
        scores.append(i)
    past = i
#print(scores)
print(sum(scores))
