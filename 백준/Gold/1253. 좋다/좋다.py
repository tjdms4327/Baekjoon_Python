import sys
input = sys.stdin.readline

n = int(input()) 
nums = list(map(int, input().split()))
nums.sort()

result = 0
for k in range(n):
    find = nums[k]
    i, j = 0, n - 1
    while i < j:
        if nums[i] + nums[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif nums[i] + nums[j] < find:
            i += 1
        else: # 두 합이 find보다 큰 경우
            j -= 1
print(result)