import sys
input=sys.stdin.readline

while True:
    s=list(input().strip().split())
    if s==['#']: break

    s[1], s[2], s[3]=int(s[1]), int(s[2]), int(s[3])
    if s[1]<31 or (s[1]==31 and (s[2]<4 or (s[2]==4 and s[3]<=30))):
        print(*s, sep=' ')
    else:
        print('?', s[1]-30, s[2], s[3])