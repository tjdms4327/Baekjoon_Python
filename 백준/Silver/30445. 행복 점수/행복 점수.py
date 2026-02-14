import sys
input = sys.stdin.readline

line = input().strip()

PH, PG = 0, 0

for char in line:
    if char in 'HAPPY':
        PH += 1
    if char in 'SAD':
        PG += 1

if PH == 0 and PG == 0:
    print("50.00")
else:
    temp = PH * 10000 // (PH + PG)
    if (PH * 100000) // (PH + PG) % 10 >= 5:
        temp += 1
    print(f"{temp/100:.2f}")
