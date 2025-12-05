import sys
input = sys.stdin.readline

zodiac = [
    ((3,21),(4,19),'Aries'),
    ((4,20),(5,20),'Taurus'),
    ((5,21),(6,20),'Gemini'),
    ((6,21),(7,22),'Cancer'),
    ((7,23),(8,22),'Leo'),
    ((8,23),(9,22),'Virgo'),
    ((9,23),(10,22),'Libra'),
    ((10,23),(11,22),'Scorpio'),
    ((11,23),(12,21),'Sagittarius'),
    ((12,22),(1,19),'Capricorn'),
    ((1,20),(2,18),'Aquarius'),
    ((2,19),(3,20),'Pisces')]

_, month, day = map(int, input().split('-'))
for (start_month, start_day), (end_month, end_day), sign in zodiac:
    if (month == start_month and day >= start_day) or (month == end_month and day <= end_day) \
        or (start_month > end_month and (month == start_month and day >= start_day or month == end_month and day <= end_day)):
        print(sign)
        break