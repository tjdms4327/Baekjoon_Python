import sys
input = sys.stdin.readline

n, k = map(int, input().split())
want = list(map(int, input().split())) # k개

for apple in want:
    if abs(apple - 1) <= abs(n - apple):
        print(1, end = ' ')
    else:
        print(n, end = ' ')