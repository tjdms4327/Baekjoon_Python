import sys
input = sys.stdin.readline

first, f = input().strip().split()
front_3_1, front_1_f = input().strip().split()
front_3_2, front_2_f = input().strip().split()
back_3_1, back_1_f = input().strip().split()
back_3_2, back_2_f = input().strip().split()
back_2, back_f = input().strip().split()

while True:
    num = input().strip()
    if num == '-1': break

    prize = 0
    if num == first:
        prize += int(f)
    
    if num[:3] == front_3_1:
        prize += int(front_1_f)
    elif num[:3] == front_3_2:
        prize += int(front_2_f)

    if num[-2:] == back_2:
        prize += int(back_f)
    if num[-3:] == back_3_1:
        prize += int(back_1_f)
    elif num[-3:] == back_3_2:
        prize += int(back_2_f)
    print(prize)