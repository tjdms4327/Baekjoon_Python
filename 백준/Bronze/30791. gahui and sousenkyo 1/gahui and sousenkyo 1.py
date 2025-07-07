def compare_score(n,list, count=0):
    for i in list:
        if n-i<=1000:
            count+=1
    return count
    
scores=list(map(int, input().split()))

print(compare_score(scores[0], scores[1:]))