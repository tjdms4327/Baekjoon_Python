import sys
input = sys.stdin.readline

m, n = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(m)]

count = 0
for x in range(m):
    for y in range(x+1, m):
        space1, space2 = space[x], space[y]
        
        tf = True
        for i in range(n):
            for j in range(i+1, n):
                if (space1[i]==space1[j] and space2[i]==space2[j])\
                    or (space1[i]<space1[j] and space2[i]<space2[j])\
                    or (space1[i]>space1[j] and space2[i]>space2[j]):
                        continue
                else:
                    tf = False
                    break
        if tf:
            count += 1
print(count)