import sys
input=sys.stdin.readline

Y, name_P=[], []
for _ in range(3):
    p, y, s=input().strip().split()
    Y.append(int(y)%100)
    name_P.append([s, int(p)])

# first method
Y.sort()
print(*Y, sep='')

# second method
name_P.sort(key=lambda x: x[1], reverse=True)
print(*[x[0][0] for x in name_P], sep='')