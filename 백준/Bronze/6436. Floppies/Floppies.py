import sys, math
input = sys.stdin.readline

case = 0
while True:   
    s = int(input())
    if s == 0:
        break
    
    case += 1
    compressed = (s + 1) // 2 
    encoded = (compressed * 3 + 1) // 2
    lines = math.ceil(encoded / 62)
    floppies = math.ceil(lines / 30000)
    
    print(f'File #{case}\nJohn needs {floppies} floppies.\n')