# bronzeI_254326
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
students = [list(input().strip().split()) for _ in range(n)]

for _ in range(m):
    question = list(input().strip().split())
    
    count = 0
    for x in students:
        if (question[0]=='-' or question[0]==x[0])\
            and (question[1]=='-' or question[1]==x[1])\
                and (question[2]=='-' or question[2]==x[2]):
                    count += 1
    print(count)