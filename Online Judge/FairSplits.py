def solution(A, B):
    for_A = A[0]
    for_B = B[0]
    ASum = sum(A)
    BSum = sum(B)
    
    count = 0
    for i in range(1,len(A)-1):
        if for_A == for_B:
            if ASum-for_A == for_A and for_B == BSum-for_B:
                #print('a',i,for_A, for_B)
                for_A += A[i]
                for_B += B[i]
                count += 1
            else:
                #print('b',i,for_A, for_B)
                for_A += A[i]
                for_B += B[i]
        elif for_A != for_B:
            #print('c',i,for_A, for_B)
            for_A += A[i]
            for_B += B[i]
    if for_A == for_B:
        if ASum-for_A == for_A and for_B == BSum-for_B:
            count += 1
            #print(ASum-for_A,for_A, for_B)
    return count
