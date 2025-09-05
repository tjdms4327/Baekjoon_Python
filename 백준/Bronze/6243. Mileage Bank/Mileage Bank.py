import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if line == '#':
        break

    mileage = 0
    while line != '0':
        origin, destination, mile, code = line.split()
        mile = int(mile)

        if code == 'F':
            mileage += 2 * mile
        elif code == 'B':
            mileage += int(1.5 * mile + 0.5)  # 안전한 반올림
        elif code == 'Y':
            mileage += mile if mile > 500 else 500

        line = input().strip()

    print(mileage)