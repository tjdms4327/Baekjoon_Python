import sys
input = sys.stdin.readline

min_t, max_t = float('inf'), float('-inf')

while True:
    line = input()
    if not line: break
        
    parts = line.split()
    for v in map(int, parts[1:]):
        min_t = min(min_t, v)
        max_t = max(max_t, v)

print(min_t, max_t)
