# bronzeII_4636
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1: break
    
    student, v = [], []
    for i in range(n):
        x, y, z, s = input().strip().split()
        student.append(s)
        v.append(int(x)*int(y)*int(z))
        
    bully_idx = v.index(max(v))
    victim_idx = v.index(min(v))
    print(f'{student[bully_idx]} took clay from {student[victim_idx]}.')