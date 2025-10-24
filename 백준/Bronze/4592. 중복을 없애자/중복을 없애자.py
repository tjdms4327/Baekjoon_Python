# bronzeII_4592
import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    
    nums = nums[1:]
    press = []
    for n in nums:
        if not press or n != press[-1]:
            press.append(n)
    print(*press, '$')