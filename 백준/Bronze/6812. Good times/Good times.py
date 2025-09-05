import sys
input = sys.stdin.readline

from datetime import datetime, timedelta

n = input().strip().zfill(4)
h, m = int(n[:2]), int(n[2:])
ottawa_time = datetime(2000, 1, 1, h, m)

# 시간대별 시차 (hours, minutes)
timezones = {
    'Ottawa': (0, 0),
    'Victoria': (-3, 0),
    'Edmonton': (-2, 0),
    'Winnipeg': (-1, 0),
    'Toronto': (0, 0),
    'Halifax': (1, 0),
    "St. John's": (1, 30)
}

for city, (dh, dm) in timezones.items():
    local_time = ottawa_time + timedelta(hours=dh, minutes=dm)
    output_time = local_time.hour * 100 + local_time.minute
    print(f"{output_time} in {city}")