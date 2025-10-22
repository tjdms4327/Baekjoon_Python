# bronzeII_32280
import sys
input = sys.stdin.readline

n = int(input())

student_time = []
for _ in range(n+1):
    time, if_student = input().strip().split()
    
    h, m = map(int, time.split(':'))
    if if_student == 'student':
        student_time.append(60*h + m)
    else:
        teacher_time = 60*h + m

h, m = map(int, input().strip().split(':'))
school_time = 60 * h + m

if school_time > teacher_time:
    standard = school_time
else:
    standard = teacher_time

print(sum(1 for i in student_time if i >= standard))