import sys
input = sys.stdin.readline

while True: 
    h = int(input())
    if h == 0:
        break
    
    sequence = [h]
    while h != 1:
        if h % 2 == 0:
            h //= 2
        else:
            h = 3*h + 1
        sequence.append(h)
    print(max(sequence))