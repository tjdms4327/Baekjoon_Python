# bronzeII_23292
import sys
input = sys.stdin.readline

birth = input().strip()
birth_digits = [birth[:4], birth[4:6], birth[6:]]

n = int(input())
max_bio = -1
max_day = ''

for _ in range(n):
    s = input().strip()
    s_digits = [s[:4], s[4:6], s[6:]]

    year_sum = sum((int(b) - int(sv))**2 for b, sv in zip(birth_digits[0], s_digits[0]))
    month_sum = sum((int(b) - int(sv))**2 for b, sv in zip(birth_digits[1], s_digits[1]))
    day_sum = sum((int(b) - int(sv))**2 for b, sv in zip(birth_digits[2], s_digits[2]))

    bio = year_sum * month_sum * day_sum

    if bio > max_bio or (bio == max_bio and s < max_day):
        max_bio = bio
        max_day = s

print(max_day)
