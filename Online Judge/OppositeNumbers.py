def solution(A):
    A = sorted(A)
    
    front = 0
    back = len(A)-1
    while front < back:
        if A[front] == -A[back]:
            return A[back]
        elif -A[front] > A[back]:
            front += 1
        elif -A[front] < A[back]:
            back -= 1
    return 0
    pass
  
  """
  solution([1, 2, 3, -4])
  0
  """
