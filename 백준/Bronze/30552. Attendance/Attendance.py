import sys
input = sys.stdin.readline

n = int(input())
student = []
for i in range(n):
    s = input().strip()
    if s == 'Present!':
        student.pop()
    else:
        student.append(s)
        
if student:
    print(*student, sep = '\n')
else:
    print("No Absences")