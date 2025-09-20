import sys

total_cents = 0
for line in sys.stdin:
    euros, cents = map(int, line.strip().split('.'))
    total_cents += euros * 100 + cents
print(f"{total_cents // 100}.{total_cents % 100:02d}")