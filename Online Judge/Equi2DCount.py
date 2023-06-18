def solution(A):
    rowtotal = [0]*len(A)
    columntotal = [0]*len(A[0])
    for i in range(len(A)):
        for j in range(len(A[0])):
            num = A[i][j]
            rowtotal[i] += num
            columntotal[j] += num
    print(rowtotal, columntotal)    
    
    cb = []
    for i in range(len(columntotal)):
        left = sum(columntotal[0:i])
        right = sum(columntotal[i+1:])
        print(left, right)
        if left == right:
            cb.append(i)
    rb = []
    for i in range(len(rowtotal)):
        left = sum(rowtotal[0:i])
        right = sum(rowtotal[i+1:])
        print(left, right)
        if left == right:
            rb.append(i)
    print(cb, rb)        
    if len(cb)>len(rb):
        return len(cb)
    elif len(cb)<len(rb):
        return len(rb)
    else:
        return 0
            
    pass
  
"""
solution([[2, 7, 5], [3, 1, 1], [2, 1, -7], [0, 2, 1], [1, 6, 8]])
[14, 5, -4, 3, 15] [8, 17, 8]
0 25
8 8
25 0
0 19
14 14
19 18
15 15
18 0
[1] [1, 3]
2
"""
