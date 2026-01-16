import sys
input = sys.stdin.readline

def parse_time(s):
    h = int(s[0:2])
    m = int(s[3:5])
    sec = int(s[6:8])
    return h, m, sec

def time_to_int(h, m, s):
    return h * 10000 + m * 100 + s

def next_second(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    return h, m, s


for _ in range(3):
    line = input().strip()
    start, end = line.split()

    sh, sm, ss = parse_time(start)
    eh, em, es = parse_time(end)

    cnt = 0
    while True:
        if time_to_int(sh, sm, ss) % 3 == 0:
            cnt += 1
        if (sh, sm, ss) == (eh, em, es):
            break
        sh, sm, ss = next_second(sh, sm, ss)
    print(cnt)
