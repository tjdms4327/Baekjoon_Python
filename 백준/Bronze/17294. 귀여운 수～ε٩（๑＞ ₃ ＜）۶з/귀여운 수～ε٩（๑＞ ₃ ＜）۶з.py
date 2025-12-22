import sys
input = sys.stdin.readline

nums = list(map(int, input().strip()))

n = len(nums)
for i in range(1, n-1):
    if nums[i-1]+nums[i+1] != 2*nums[i]:
        print("흥칫뿡!! <(￣ ﹌ ￣)>")
        sys.exit()
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")