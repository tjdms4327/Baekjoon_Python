import sys
input = sys.stdin.readline

while True:
    nums = list(map(float, input().split()))
    if sum(nums) == 0: break

    d, w_resolution, h_resolution = nums
    w, h = 16*d/(337**0.5), 9*d/(337**0.5)
    print(f'Horizontal DPI: {w_resolution/w:.2f}')
    print(f'Vertical DPI: {h_resolution/h:.2f}')