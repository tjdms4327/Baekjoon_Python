import sys
input = sys.stdin.readline

n, m = map(int, input().split())

song = {}
for _ in range(n):
    line = input().strip().split()
    t = int(line[0])
    s = line[1]
    A = ''.join(list(line[2:])[:3])
    
    if A in song:
        song[A] = '?'
    else:
        song[A] = s

for _ in range(m):
    s = ''.join(list(input().strip().split()))
    if s in song:
        print(song[s])
    else:
        print('!')