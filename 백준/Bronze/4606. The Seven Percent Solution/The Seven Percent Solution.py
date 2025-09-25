# bronzeII_4606
import sys
input = sys.stdin.readline

while True:  
    s = input().strip()
    if s == '#': break
    
    s = s.replace('%', '%25').replace(' ', '%20').replace('!', '%21').replace('$', '%24').replace('(', '%28').replace(')', '%29').replace('*', '%2a')
    print(s)