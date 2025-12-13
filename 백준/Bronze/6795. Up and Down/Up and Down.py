import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

niki, byron = 0, 0
sn, sb = s, s
while sn > 0:
    niki += min(a, sn)
    sn -= min(a, sn)
    if sn <= 0:
        break
    
    niki -= min(b, sn)
    sn -= min(b, sn)
while sb > 0:
    byron += min(c, sb)
    sb -= min(c, sb)
    if sb <= 0:
        break
    
    byron -= min(d, sb)
    sb -= min(d, sb)
    
if niki > byron:
    print('Nikky')
elif niki == byron:
    print('Tied')
else:
    print('Byron')