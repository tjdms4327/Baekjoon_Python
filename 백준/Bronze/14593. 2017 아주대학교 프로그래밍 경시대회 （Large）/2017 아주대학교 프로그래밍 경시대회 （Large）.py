# bronzeII_14593
import sys
input = sys.stdin.readline

n = int(input())

students = []
for i in range(1, 1+n):
    scl = list(map(int, input().split()))
    students.append([i]+scl)
    
students.sort(key = lambda x:(-x[1], x[2], x[3]))
print(students[0][0])