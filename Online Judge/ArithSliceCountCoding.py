def solution(A):
    count = 0
    for i in range(len(A)-2):
        for j in range(i+1, len(A)-1):
            if A[i+1]-A[i] == A[j+1]-A[j]:
                count += 1
            else:
                break
                
    if count > 1000000000:
        return -1
    else:
        return count
    pass
