import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time = int((24 * 60) * (m / n))
hours = time // 60
minutes = time % 60
print(f'{hours:02d}:{minutes:02d}')