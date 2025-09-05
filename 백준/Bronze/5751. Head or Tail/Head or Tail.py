import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break

    nums = list(map(int, input().split()))
    mary = nums.count(0)
    print(f'Mary won {mary} times and John won {n-mary} times')