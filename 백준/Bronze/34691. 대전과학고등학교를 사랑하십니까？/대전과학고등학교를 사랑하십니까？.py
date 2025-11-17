# bronzeV_34691
import sys
input = sys.stdin.readline

answer = {'animal': 'Panthera tigris', 
          'flower': 'Forsythia koreana',
          'tree': 'Pinus densiflora'}

while True:
    q = input().strip()
    if q == 'end':
        break
    
    print(answer[q])

