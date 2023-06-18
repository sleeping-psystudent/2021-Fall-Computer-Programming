def solution(N, K):
    # write your code in Python 3.6
    if (N-K)<0 or N<0 or K<0:
        return -1
    elif (N-K) == 0 or K == 0:
        return 1

    if N-K>K:
        K = N-K
    factorial = 1
    for i in range(1,N-K+1):
        factorial *= i
    factorial2 = factorial
    for j in range(N-K+1,K+1):
        factorial *= j
    factorial3 = factorial
    for h in range(K+1,N+1):
        factorial *= h
    factorial4 = factorial

    result = factorial4//factorial2//factorial3
    if result>1000000000:
        return -1
    else:
        return result
    pass
