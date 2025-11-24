import sys
input = sys.stdin.readline

h0, m0 = map(int, input().split())
h1, m1 = map(int, input().split())

start = h0*60 + m0
end = h1 * 60 + m1

n = input().strip()
count = 0
for t in range(start, end+1):
    h = t//60
    m = t % 60
    if n in f'{h:02d}:{m:02d}':
        count += 1
print(count)