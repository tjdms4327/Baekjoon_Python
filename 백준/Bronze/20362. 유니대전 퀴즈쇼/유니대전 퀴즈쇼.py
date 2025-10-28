# bronzeI_20362
import sys
input = sys.stdin.readline

n, winner = input().strip().split()

chat = {}
for _ in range(int(n)):
    name, content = input().strip().split()
    
    if name == winner:
        sys.stdin.read()
        if content in chat:
            print(chat[content])
        else:
            print(0)
        sys.exit()
    
    if content in chat:
        chat[content] += 1
    else:
        chat[content] = 1