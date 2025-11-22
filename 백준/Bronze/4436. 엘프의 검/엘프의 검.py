import sys

for line in sys.stdin.read().splitlines():
    x = int(line)
    
    n = x
    lst = []
    while len(lst) < 10:
        for i in str(n):
            if i not in lst:
                lst.append(i)
        if len(lst) == 10:
            break
        n += x
    print(n//x)