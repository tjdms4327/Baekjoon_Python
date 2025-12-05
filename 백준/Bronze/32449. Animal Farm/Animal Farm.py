import sys
input = sys.stdin.readline

n = int(input())
animals = []
pig = 0
for _ in range(n):
    a, count = input().strip().split()
    count = int(count)
    
    if a == 'pig':
        pig = max(pig, count)
    else:
        animals.append(count)

print(pig + sum(x for x in animals if x<pig))