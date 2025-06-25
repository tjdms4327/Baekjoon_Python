x, y, w, h = map(int, input().split())

print(min(abs(x - w), abs(y - h), min(x, y)))