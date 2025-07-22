def print_pattern(pattern, k):
    for _ in range(k):
        print(pattern)
        
k=int(input())    
print_pattern('G' * k + '...' * k, k)
print_pattern('.' * k + 'I' * k + '.' * k + 'T' * k, k)
print_pattern('..' * k + 'S' * k + '.' * k, k)