# bronzeIII_3234
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
k = int(input())
s = list(input().strip())

tx, ty = 0, 0
heard = []
if x - 1 <= tx <= x + 1 and y - 1 <= ty <= y + 1:
    heard.append(0)

for j in range(k):
    move = s[j]
    if move == 'I':  
        tx += 1
    elif move == 'Z':
        tx -= 1
    elif move == 'S':
        ty += 1
    elif move == 'J':
        ty -= 1

    if x - 1 <= tx <= x + 1 and y - 1 <= ty <= y + 1:
        heard.append(j + 1)

if heard:
    print(*heard, sep='\n')
else:
    print(-1)