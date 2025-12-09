import sys
input = sys.stdin.readline

while True:
    lst = list(map(int, input().split()))
    n = lst[0]
    if n == 0:
        break
    
    new_lst = [0] + lst[1:]
    
    nums = []
    for i in range(1, n+1):
        count = new_lst[i]-new_lst[i-1]
        nums.extend([i]*count)
    print(*nums)