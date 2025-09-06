import sys
input = sys.stdin.readline

from collections import Counter

for case in range(1, int(input())+1):
    print(f'Case {case}:')

    students = [int(input()) for _ in range(int(input()))]
    for grade in students:
        new_grade = grade + 1
        if 1 <= new_grade <= 6:
            print(new_grade)