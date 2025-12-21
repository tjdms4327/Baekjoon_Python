import sys
input = sys.stdin.readline

while True:   
    name, f = input().strip().split()
    if name=='#' and f=='0':
        break
    
    f = int(f)
    print(f'{name} Library')
    c = int(input())
    for idx in range(1, c+1):
        w, text = input().strip().split()
        text_width = len(text)*f+2
        w = int(w)
        
        if text_width <= w:
            print(f'Book {idx} horizontal')
        else:
            print(f'Book {idx} vertical')