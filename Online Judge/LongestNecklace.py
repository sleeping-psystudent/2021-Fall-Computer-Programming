def solution(A):
    total = []
    i = 0
    j = A[i]
    maxnum = 0
    tem = []
    
    while len(total) != len(A):
        t = i
        j = A[i]
        tem.append(i)
        while t != j:
            i = j
            j = A[i]
            tem.append(i)
            #print(t, i, j)
        if len(tem) > maxnum:
            maxnum = len(tem)
        total += tem
        tem.clear()
        
        i = j+1
        total.sort()
        for m in range(len(total)):
            if i == total[m]:
                i += 1
        #print(i, total)
        
    #print(maxnum)
    return maxnum
        
    pass
