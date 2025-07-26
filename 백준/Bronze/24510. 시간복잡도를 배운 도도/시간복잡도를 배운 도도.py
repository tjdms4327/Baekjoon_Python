import sys
input=sys.stdin.readline

import re

n=int(input())
for_while=[len(re.findall('for|while', input().strip())) for _ in range(n)]
print(max(for_while))