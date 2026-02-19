import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
count = {}
answer = 0
for right in range(n):
    count[arr[right]] = count.get(arr[right], 0) + 1
    
    while len(count) > 2:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            del count[arr[left]]
        left += 1
    
    answer = max(answer, right - left + 1)

print(answer)
