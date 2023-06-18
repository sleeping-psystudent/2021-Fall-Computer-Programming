def solution(A):
    
    if len(A) == 0:
        return False
    
    frontSum, backSum = A[0], A[-1]
    total = sum(A)
    
    start = 1
    recal = -2    
    
    while start != len(A)+recal:
        
        if frontSum == backSum and backSum == total - (frontSum + backSum) - (A[start]+A[recal]):
            return True
        elif frontSum > total - (frontSum + backSum) - (A[start]+A[recal]) or backSum > total - (frontSum + backSum) - (A[start]+A[recal]):
            return False
        elif frontSum > backSum:
            backSum += A[recal]
            recal -= 1
        elif backSum > frontSum:
            frontSum += A[start]
            start += 1
        elif backSum == frontSum:
            backSum += A[recal]
            recal -= 1
            frontSum += A[start]
            start += 1
            
    pass
