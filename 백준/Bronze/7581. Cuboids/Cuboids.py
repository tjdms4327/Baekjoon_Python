import sys
input = sys.stdin.readline

while True:
    s = list(map(int, input().split()))
    if s == [0, 0, 0, 0]: break

    l, w, h, v = s
    if v == 0:
        print(l, w, h, l*w*h)
    elif l == 0:
        missing = v // (w*h)
        print(missing, w, h, v)
    elif w == 0:
        missing = v // (l*h)
        print(l, missing, h, v)
    else: # h == 0
        missing = v // (w*l)
        print(l, w, missing, v)