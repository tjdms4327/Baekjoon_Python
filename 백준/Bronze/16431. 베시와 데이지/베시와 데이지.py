import sys
input=sys.stdin.readline

B = list(map(int, input().strip().split()))
D = list(map(int, input().strip().split()))
J = list(map(int, input().strip().split()))

# 대각선 이동은 x, y 좌표이동 중 min값,
# 상하좌우 이동은 max값에서 위에서 구한 min값 빼면됨
# min + (max-min) 이니까 그냥 max값으로.
move_B=max(abs(B[0]-J[0]), abs(B[1]-J[1]))
move_D=abs(D[0]-J[0])+abs(D[1]-J[1])

#print(move_B, move_D)
if move_B<move_D: print('bessie')
elif move_B==move_D: print('tie')
else: print('daisy')