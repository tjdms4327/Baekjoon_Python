import sys
input = sys.stdin.readline

while True:   
    seat, now = input().strip().split()
    if seat=='#' and now=='0':
        break
    now = int(now)
    
    while True:   
        command, n = input().strip().split()
        if command=='X' and n=='0':
            break
        
        n = int(n)
        if command == 'B':
            if now+n <= 68:
                now += n
        elif command == 'C':
            if n <= now:
                now -= n
        
    print(seat, now)