t1,m1,t2,m2=map(int, input().split())

if t1>t2 or (t1==t2 and m1>m2):
    t2+=24
if m1>m2:
    m2+=60
    t2-=1
minutes=(t2-t1)*60+(m2-m1)
print(minutes, minutes//30)