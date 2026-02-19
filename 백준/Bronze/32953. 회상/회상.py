import sys
input = sys.stdin.readline

n, m = map(int, input().split())

students = []
for _ in range(n):
    k = int(input())
    nums = list(input().strip().split())
    students.extend(nums)
    
cand = set(students)
cnt = 0
for x in cand:
    if students.count(x) >= m:
        cnt += 1
        
print(cnt)