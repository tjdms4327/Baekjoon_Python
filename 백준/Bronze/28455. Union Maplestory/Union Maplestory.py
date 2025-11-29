import sys
input = sys.stdin.readline

level = [60, 100, 140, 200, 250]

n = int(input())

L = [int(input()) for _ in range(n)]
L.sort(reverse = True)

total = 0
increase = 0    
for i in range(min(42, n)):
    l = L[i]
    total += l
    for x in level:
        if l >= x:
            increase += 1
        else:
            break
print(total, increase)