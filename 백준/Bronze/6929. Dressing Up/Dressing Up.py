import sys
input = sys.stdin.readline

h = int(input())
top = []
for i in range(1, 1+h//2):
    temp = '*'*(2*i-1) + ' '*(2*h - 2*(2*i-1)) + '*'*(2*i-1)
    top.append(temp)

print(*top, sep='\n')
print('*'*(2*h))
print(*top[::-1], sep='\n')