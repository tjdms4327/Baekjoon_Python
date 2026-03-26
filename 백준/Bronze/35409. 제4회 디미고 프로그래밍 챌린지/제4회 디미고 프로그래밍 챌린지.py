import sys
input = sys.stdin.readline

h, m = map(int, input().split())
time = h*60 + m

if 6*60+30<=time<=9*60\
    or 9*60+50<=time<=10*60\
    or 10*60+50<=time<=11*60\
    or 11*60+50<=time<=12*60\
    or 12*60+50<=time<=13*60+50\
    or 14*60+40<=time<=14*60+50\
    or 15*60+40<=time<=15*60+50\
    or 16*60+40<=time<=22*60+50:
        print('Yes')
else:
    print('No')