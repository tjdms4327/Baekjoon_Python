import sys
input=sys.stdin.readline
import re

s=input().strip()
zeros=re.findall(r'0+',s)
ones=re.findall(r'1+',s)

print(min(len(zeros), len(ones)))