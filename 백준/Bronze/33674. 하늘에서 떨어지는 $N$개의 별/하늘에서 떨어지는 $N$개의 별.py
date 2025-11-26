import sys
input = sys.stdin.readline

n, d, k = map(int, input().split())
stars = list(map(int, input().split()))

standard = max(stars)
star = 0
clean = 0
for _ in range(d):
    if star + standard > k:
        clean += 1
        star = 0
    star += standard
print(clean)