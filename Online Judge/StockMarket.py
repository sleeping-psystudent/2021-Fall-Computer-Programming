def solution(A):
    minN = A[0]
    maxP = 0
    for i in range(1, len(A)):
        if A[i] > minN:
            maxP = max(maxP, A[i]-minN)
        else:
            minN = A[i]
    return maxP
    pass
  
  """
  solution([108,102,86,63,81,101,94,106,101])
  43
  """
