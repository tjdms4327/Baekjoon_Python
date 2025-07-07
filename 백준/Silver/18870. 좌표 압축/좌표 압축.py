n=int(input())
nums=list(map(int, input().split()))

new=sorted(set(nums))
index_map={value: idx for idx, value in enumerate(new)}
for i in nums:
    print(index_map[i], end=' ')