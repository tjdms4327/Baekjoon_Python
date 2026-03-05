import sys
input = sys.stdin.readline

mushroom = [int(input()) for _ in range(8)]

mushroom += mushroom
MAX = -1
for i in range(8):
    half = sum(mushroom[i:i+4])
    MAX = max(MAX, half)
print(MAX)