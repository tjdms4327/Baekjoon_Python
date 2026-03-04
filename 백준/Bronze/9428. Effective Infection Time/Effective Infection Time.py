import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    infection = list(map(int, input().split()))
    attack = list(map(int, input().split()))
    
    if infection[1] == attack[1]:
        total_months = 12 - infection[0] + 1
        per_month = 0.5 / total_months
        passed_months = attack[0] - infection[0]
        elt = per_month * passed_months
    else:
        elt = 0.5
        
        full_years = attack[1] - infection[1] - 1
        elt += full_years
        elt += (attack[0] - 1) / 12
        
    print(f'{elt:.4f}')