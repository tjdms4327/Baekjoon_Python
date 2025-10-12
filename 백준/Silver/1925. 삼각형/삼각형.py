# silverIV_1925
import sys
input = sys.stdin.readline

def judge_angle(side_double):
    if side_double[0] + side_double[1] == side_double[2]:
        return 'Jikkak'
    elif side_double[0] + side_double[1] < side_double[2]:
        return 'Dunkak'
    else:
        return 'Yeahkak'

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

ABx, ABy = B[0]-A[0], B[1]-A[1]
ACx, ACy = C[0]-A[0], C[1]-A[1]
if ABx*ACy - ABy*ACx == 0:
    print('X')
    exit()

double_AB = (A[0] - B[0])**2 + (A[1] - B[1])**2
double_BC = (B[0] - C[0])**2 + (B[1] - C[1])**2
double_CA = (C[0] - A[0])**2 + (C[1] - A[1])**2
side_double = [double_AB, double_BC, double_CA]
side_double.sort()

if len(set(side_double)) == 1:
    print('JungTriangle')
else:
    angle = judge_angle(side_double)
    if len(set(side_double)) == 2:
        print(angle+'2Triangle')
    else:
        print(angle+'Triangle')