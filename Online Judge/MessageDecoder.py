def solution(S):
    if S[0]=='0':
        return 0
    c = [1, 1]
    for i in range(2, len(S)+1):
        c.append(0)        
        if int(S[i-1]) > 0:
            c[i] = c[i-1]
        if int(S[i-2]+S[i-1]) in range(10,27):
            c[i] += c[i-2]
    return c[-1]   
    pass
  
  """
  solution('2611055971756562')
  4
  """
