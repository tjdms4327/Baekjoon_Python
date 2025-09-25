# bronzeII_4176
import sys
input = sys.stdin.readline

while True:  
    s = input().strip()
    if s =='END': break
    
    x_prev = s
    count = 0
    while True:
        x_curr = str(len(x_prev))
        count += 1
        if x_curr == x_prev:
            print(count)
            break
        x_prev = x_curr