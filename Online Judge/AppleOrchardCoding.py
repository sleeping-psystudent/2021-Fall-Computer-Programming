def finding(A, k, l):
    if k+l>len(A):
        return -1
    s = [0]*1000
    s[0] = A[0]
    for i in range(1, len(A)):
        s[i] = s[i-1]+A[i]
    
    mx = -1
    x = 0
    y = 0
    for i in range(len(A)+1-k):
        if i>0:
            x = s[i+k-1]-s[i-1]
        else:
            x = s[i+k-1]
        for j in  range(i+k, len(A)-l+1):
            if j>0:
                y = s[j+l-1]-s[j-1]
            else:
                y = s[b+l-1]
            if(x+y)>mx:
                mx = x+y
    return mx
def solution(A, K, L):
    a1 = finding(A, K, L)
    a2 = finding(A, L, K)
    return max(a1, a2)
    pass
  
"""
A = [6,1,4,6,3,2,7,4]
K = 3
L = 2

solution(A, K, L)
24
  """
