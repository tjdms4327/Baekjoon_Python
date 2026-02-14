import sys
input = sys.stdin.readline

n = int(input())

rings = {}
for _ in range(n):
    p, s = input().strip().split()
    
    if s != '-':
        if s not in rings:
            rings[s] = [p]
        else:
            rings[s].append(p)
            
count = 0
result = []
for names in rings.values():
    if len(names)==2:
        result.append(names)
        count += 1
        
print(count)
if count != 0:
    for x in result:
        print(*x)