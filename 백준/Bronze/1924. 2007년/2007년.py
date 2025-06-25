import sys
input=sys.stdin.readline

def day():
    tot=0
    days=['SUN','MON','TUE','WED','THU','FRI','SAT']
    for i in range(1,x):
        if i==2:
            tot+=28
        elif i in [1,3,5,7,8,10,12]:
            tot+=31
        else:
            tot+=30
    tot+=y
    return days[tot%7]

x,y=map(int, input().split())
print(day())