def solution(A):
    A = sorted(A)
    m = 0
    for i in range(len(A)-1):
        if A[i+1]-A[i] > m:
            m = A[i+1]-A[i]
    return round((m-1)/2)
    pass
  
  """
  solution([5, 5])
  0
  """
