import sys
input = sys.stdin.readline

n=int(input())
max_pay, Russia_name=0,''
for _ in range(n):
    pay, name, nation=input().strip().split()
    pay=int(pay)

    if nation=='Russia' and max_pay<pay:
        max_pay=pay
        Russia_name=name

print(Russia_name)    