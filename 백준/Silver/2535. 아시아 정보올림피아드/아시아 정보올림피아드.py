import sys
input = sys.stdin.readline

n = int(input())
students = [tuple(map(int, input().split())) for _ in range(n)]

students.sort(key=lambda x: -x[2])

medal_count = {}  
medalists = []

for country, stu_num, score in students:
    if medal_count.get(country, 0) < 2:
        medalists.append((country, stu_num))
        medal_count[country] = medal_count.get(country, 0) + 1
    if len(medalists) == 3:
        break

for m in medalists:
    print(*m)