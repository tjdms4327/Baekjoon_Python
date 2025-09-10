import sys
input = sys.stdin.readline

n = int(input())
start_index, end_index = 1, 1
sum = 1 # 1에서부터 시작
count = 1 # n일 경우

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else: # sum < n
        end_index += 1
        sum += end_index
print(count)