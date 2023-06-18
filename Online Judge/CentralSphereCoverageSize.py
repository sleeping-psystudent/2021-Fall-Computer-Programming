def solution(A):
    if len(A) == 0:
        return 0
    st = []
    for num in A:
        R2 = (num[0]**2 + num[1]**2 + num[2]**2)
        st.append(R2)
    con = set(st)
    return len(con)
    pass
  
  """
  solution([(0, 5, 4), (0, 0, -3), (-2, 1, -6), (1, -2, 2), (1, 1, 1), (4, -4, 3)])
  3
  """
