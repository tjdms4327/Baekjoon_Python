import sys
input=sys.stdin.readline

mapping={
    'Paper':57.99, 
    'Printer':120.50,
    'Planners':31.25,
    'Binders':22.50,
    'Calendar':10.95,
    'Notebooks':11.20,
    'Ink':66.95
}

price=0
while True:
    s=input().strip()
    if s=='EOI': break
        
    price+=mapping[s]
    
print(f'${price}')