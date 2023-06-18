def solution(A):
    minN = 101
    for i in range(1,7):
        count = 0
        for num in A: 
            if num == 7-i:
                count += 2
            elif num != 7-i and num != i:
                count += 1
        minN = min(minN, count)
            
    return minN
  
  """
  solution([1,6,2,3]) # maxc:2, minc:1
  3
  """
