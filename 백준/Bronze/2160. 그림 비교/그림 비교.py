# bronzeI_2160
import sys
input = sys.stdin.readline

n = int(input())
pictures = []
for _ in range(n):
    matrix = [list(input().strip()) for _ in range(5)]
    pictures.append(matrix)
    
diff = {}
for x in range(n):
    for y in range(x+1, n):
        picture1 = pictures[x]
        picture2 = pictures[y]
        
        count = 0
        for row in range(5):
            if picture1[row] != picture2[row]:
                count += sum(i != j for i, j in zip(picture1[row], picture2[row]))
        diff[str(x+1)+' '+str(y+1)] = count

print(min(diff, key = diff.get))