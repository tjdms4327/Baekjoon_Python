import sys
input = sys.stdin.readline

while True:
    name1, name2 = input().strip().split()
    if name1 == name2 == '#':
        break
    
    n = int(input())
    one, two = 0, 0
    for _ in range(n):
        a, b = input().strip().split()
        if a == b:
            one += 1
        else:
            two += 1
            
    print(f'{name1} {one} {name2} {two}')