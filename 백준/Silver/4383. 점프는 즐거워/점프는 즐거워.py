import sys
input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    
    nums = list(map(int, line.split()))
    n = nums[0]
    arr = nums[1:]
    
    if n == 1:
        print('Jolly')
        continue
    
    diff = set([abs(arr[i] - arr[i-1]) for i in range(1, n)])
    if diff == set(range(1, n)):
        print('Jolly')
    else:
        print('Not jolly')