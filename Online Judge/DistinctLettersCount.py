def solution(S):
    data = {}
    S = list(S)
    if len(S) == 0:
        return 0
    
    for i in range(len(S)):
        data[S[i]] = data.get(S[i],0)+1
    
    how_many = list(data.values())
    
    if len(how_many) == 1:
        return 0
    
    else:
        how_many.sort(reverse = True)    
        s = how_many[0]-1
        count2 = 0
        for j in range(len(how_many)-1):
            if how_many[j+1]>=s:
                count2 += how_many[j+1]-s
                if s > 0:
                    s -= 1 
                else:
                    s = 0
        return count2
