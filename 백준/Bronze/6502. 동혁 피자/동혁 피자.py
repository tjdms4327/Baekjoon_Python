import sys
input = sys.stdin.readline

case = 0
while True:
    nums = list(map(int, input().split()))
    if nums == [0]: break

    r, w, l = nums
    case += 1
    if w**2 + l**2 <= 4 * r**2:
        print(f'Pizza {case} fits on the table.')
    else:
        print(f'Pizza {case} does not fit on the table.')