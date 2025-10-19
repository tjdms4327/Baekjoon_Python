# bronzeI_1032
import sys
input = sys.stdin.readline

n = int(input())
file_names = [input().strip() for _ in range(n)]

find = ''
for col in zip(*file_names):
    if len(set(col)) == 1:
        find += col[0]
    else:
        find += '?'
print(find)