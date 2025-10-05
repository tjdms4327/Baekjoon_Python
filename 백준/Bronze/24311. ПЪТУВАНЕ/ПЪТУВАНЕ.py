# bronzeIII_24311
import sys
input = sys.stdin.readline

start_h, start_m = map(int, input().split())
start = 60*start_h + start_m
start -= 10 # 10분 전 도착해야 함

register = int(input())
move_h, move_m = map(int, input().split())
student = int(input())
accomodate = int(input())
time = register + (60*move_h + move_m) + (student+1) * accomodate
start -= time

if start < 0:
    start += 60*24
print(f'{start//60:02d} {start%60:02d}')