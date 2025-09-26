# bronzeII_5715
import sys
input = sys.stdin.readline

mapping = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8,
           'S':1/16, 'T':1/32, 'X':1/64}

while True:  
    s = input().strip()
    if s == '*': break
    
    node = list(s.split('/'))
    count = 0
    for i in node:
        time = sum(mapping[j] for j in i)
        if time == 1:
            count += 1
    print(count)