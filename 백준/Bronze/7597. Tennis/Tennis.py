import sys
input = sys.stdin.readline

while True:  
    line = input().strip()
    if line == '#':
        break
    
    A, B = 0, 0
    a, b = 0, 0
    for x in line:
        if x == 'A':
            a += 1
        elif x == 'B':
            b += 1
        
        if max(a, b)>=4 and abs(a-b)>=2:
            if a > b:
                A += 1
            elif a < b:
                B += 1
            
            a, b = 0, 0
    print(f'A {A} B {B}')