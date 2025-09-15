import sys
input = sys.stdin.readline

while True: 
    l, w, a = list(map(int, input().split()))
    if l+w+a == 0: break
    
    if l == 0:
        l = a // w
    elif w == 0:
        w = a // l
    else: # a == 0
        a = l * w
    print(l, w, a)