import sys
input = sys.stdin.readline

n = int(input())

m, j = [], []
for _ in range(n):
    name, p = input().strip().split()
    p = int(p)
    
    if name == 'M':
        m.append(p)
    else:
        j.append(p)
        
M = sum(m) / len(m) if m else 0
J = sum(j)/len(j) if j else 0
if M > J:
    print('M')
elif M == J:
    print('V')
else:
    print('J')