import sys
input = sys.stdin.readline

while True:  
    line = input().strip()
    if line == '#':
        break
    
    nums = list(map(int, line))[::-1]
    
    tot = 0
    for i in range(len(nums)):
        tot += nums[i] * (i+2)
    check = 11 - tot % 11
    
    if 1 <= check <= 9:
        result = check
    elif check == 10:
        result = 'Rejected'
    elif check == 11:
        result = 0
    print(f'{line} -> {result}')