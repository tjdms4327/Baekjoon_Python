# bronzeII_7513
import sys
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    print(f'Scenario #{case}:')
    
    m = int(input())
    words = [input().strip() for _ in range(m)]
    
    n = int(input())
    for _ in range(n):
        nums = list(map(int, input().split()))
        k = nums[0]
        result = ''
        for i in nums[1:]:
            result += words[i]
        print(result)
    print()