import sys
input = sys.stdin.readline

x1,y1,x2,y2,x3,y3 = map(float, input().split())

if (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1) == 0: # 외적 == 0 (한 직선)
    print(-1)
else:
    AB = ((x1-x2)**2 + (y1-y2)**2)**0.5
    AC = ((x1-x3)**2 + (y1-y3)**2)**0.5
    BC = ((x2-x3)**2 + (y2-y3)**2)**0.5

    circumstances = [2*(AB+AC), 2*(AB+BC), 2*(AC+BC)]
    print(max(circumstances) - min(circumstances))