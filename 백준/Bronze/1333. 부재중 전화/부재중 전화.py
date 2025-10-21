# bronzeI_1333
import sys
input = sys.stdin.readline

n, l, d = map(int, input().split())

total = n * (l+5) - 5

t = 0
while True:  
    if t > total:
        print(t)
        break
    
    song_num = t // (l+5)
    song_in_time = t % (l+5)
    if song_in_time >= l:
        print(t)
        break
    t += d