# bronzeII_3076.py
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
a, b = map(int, input().split())

row_pattern = ""
for col in range(c):
    if col % 2 == 0:
        row_pattern += "X" * b
    else:
        row_pattern += "." * b

for row in range(r):
    for _ in range(a):
        if row % 2 == 0:
            print(row_pattern)
        else: # 색 반전
            print(row_pattern.replace("X", "t").replace(".", "X").replace("t", "."))