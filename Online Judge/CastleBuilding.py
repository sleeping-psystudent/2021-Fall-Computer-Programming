def solution(A):
    #c = set(A)
    #if len(c) == 1:
    #    return 1
    castle = 1 
    #pos = 0
    #neg = 0
    last = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            #pos += 1
            #if neg != 0:
            if last != 1:
                #neg = 0
                castle += 1
            last = 1
        elif A[i] > A[i+1]:
            #neg += 1
            #if pos != 0:
            if last != -1:
                #pos = 0
                castle += 1
            last = -1
        #print(pos, neg)
        
    #if len(A) >= 2:
    #    castle += 1
    return castle    
    # return pos + neg + 1
    pass
  
"""
print(solution([1]))                   # 1
print(solution([1,2]))                 # 2
print(solution([1,1,1]))               # 1
print(solution([1,2,1]))               # 3
print(solution([1,2,6]))               # 2
print(solution([1,2,3,4,4,3,4,4,5,6])) # 4
print(solution([-10,2,2,2,2]))         # 2
print(solution([1,0,0,0,1]))           # 3
print(solution([0,1,0,1,0]))           # 5
print(solution([0,2,2,1,1,0,0]))       # 3
1
2
1
3
2
4
2
3
5
3
"""
