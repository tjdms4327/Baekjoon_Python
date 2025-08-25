import sys
input = sys.stdin.readline

def phy_score(height, weight):
    bmi = weight / (height/100)**2
    
    if height < 140.1:
        return 6
    elif height < 146:
        return 5
    elif height < 159:
        return 4
    elif height < 161: 
        if 16.0 <= bmi < 35.0:
            return 3
        else: return 4
    elif height < 204:
        if 20.0 <= bmi < 25.0:
            return 1
        elif (18.5 <= bmi < 20.0) or (25.0 <= bmi < 30.0):
            return 2
        elif (16.0 <= bmi < 18.5) or (30.0 <= bmi < 35.0):
            return 3
        else: return 4
    else: return 4

t = int(input())
for _ in range(t):
    h, w = map(float, input().split())
    print(phy_score(h, w))
