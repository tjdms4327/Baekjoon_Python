# bronzeII_31496
import sys
input = sys.stdin.readline

n, s = input().strip().split()

deleted_item = 0
for _ in range(int(n)):
    name, count = input().strip().split()
    name_lst = list(name.split('_'))
    
    if s in name_lst:
        deleted_item += int(count)

print(deleted_item)