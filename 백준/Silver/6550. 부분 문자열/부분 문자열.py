# silverV_6550
import sys
from collections import deque

for line in sys.stdin.read().splitlines():
    if not line:
        continue
    s, t = line.split()
    s = deque(s)
    
    for i in t:
        if s and i == s[0]:
            s.popleft()
            
    if not s:
        print('Yes')
    else:
        print('No')