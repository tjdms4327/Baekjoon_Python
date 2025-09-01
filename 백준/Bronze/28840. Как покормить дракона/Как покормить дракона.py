import sys
input = sys.stdin.readline

from datetime import datetime, timedelta
fmt = '%H:%M'

today = datetime.strptime(input().strip(), fmt)
tomorrow = datetime.strptime(input().strip(), fmt)
tomorrow += timedelta(days=1)

delta = int((tomorrow - today).total_seconds() // 60)
print(f'{delta//60:02d}:{delta%60:02d}')