import sys
input = sys.stdin.readline

for case in range(int(input())):
    row = [0]*9
    piece = list(map(int, input().split()))
    for i in range(2, len(piece), 2):
        row[piece[i]] += 1
    print(max(row))