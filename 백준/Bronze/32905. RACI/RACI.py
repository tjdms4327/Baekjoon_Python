import sys
input=sys.stdin.readline

n, m=map(int, input().strip().split())
defalt="Yes"
for _ in range(n):
    students=list(input().strip().split())
    if students.count("A")!=1: defalt='No'
print(defalt)