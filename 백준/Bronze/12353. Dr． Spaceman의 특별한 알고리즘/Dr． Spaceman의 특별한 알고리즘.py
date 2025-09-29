# bronzeII_12353
import sys, math
input = sys.stdin.readline

t = int(input())
for case in range(1, t+1):
    sex, h1, h2 = input().split()
    h1 = list(map(int, h1.replace("'", " ").replace('"', '').split()))
    h2 = list(map(int, h2.replace("'", " ").replace('"', '').split()))
    
    mom = h1[0]*12 + h1[1]
    dad = h2[0]*12 + h2[1]
    H = mom + dad

    if sex == 'B':
        H += 5
    else:
        H -= 5
    H /= 2

    low = math.ceil(H - 4)
    high = math.floor(H + 4)
    print(f'Case #{case}: {low//12}\'{low%12}" to {high//12}\'{high%12}\"')