import sys, math
input = sys.stdin.readline

h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())

def destroy_time(hp, dmg, reload):
    shots = math.ceil(hp / dmg)
    return 0.5 + (shots-1) * reload

time1 = destroy_time(h2, d1, t1)  
time2 = destroy_time(h1, d2, t2)  
if abs(time1 - time2) < 1e-9:
    print("draw")
elif time1 < time2:
    print("player one")
else:
    print("player two")