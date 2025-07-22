import sys
input = sys.stdin.readline
from collections import Counter

n=int(input())
nums=[int(input()) for _ in range(n)]
nums.sort()

# 산술평균
print(round(sum(nums)/n))

# 중앙값
print(nums[n//2]) # n 홀수니까

# 최빈값
counter = Counter(nums)
freq = counter.most_common()  # [(숫자, 빈도), ...]
max_freq = freq[0][1]
modes = [num for num, cnt in freq if cnt == max_freq] # 최빈값 후보
modes.sort()
if len(modes) == 1:
    print(modes[0])
else:
    print(modes[1])

# 범위
print(nums[-1] - nums[0])