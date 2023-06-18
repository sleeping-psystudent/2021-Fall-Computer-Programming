def solution(T):
    if len(T)==0:
        return 0
    l = len(T)
    peak = T[0]
    whole = T[0]
    period = 0
    
    for tem in T:
        if tem <= peak:
            peak = whole
        elif tem > whole:
            whole = tem
    for tem in T:
        if tem <= peak:
            period += 1
    return period
  
  if __name__ == "__main__":
    q = [int(i) for i in input().split('_')]
    print(solution(q))
    
"""
-5_-5_-5_-42_6_120
4
"""
