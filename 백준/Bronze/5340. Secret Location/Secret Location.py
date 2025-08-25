import sys
input = sys.stdin.readline

cnt = [len(input().strip()) for _ in range(6)]

print(f'Latitude {cnt[0]}:{cnt[1]}:{cnt[2]}')
print(f'Longitude {cnt[-3]}:{cnt[-2]}:{cnt[-1]}')