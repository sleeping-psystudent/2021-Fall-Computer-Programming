def solution(A):
    maxBanner = 0    
    orgA = set(A)
    
    for n in orgA:
        count = 0
        for h in A:
            if h >= n:
                count += 1
            else:
                if count*n > maxBanner:
                    maxBanner = count*n
                count = 0
        if count*n > maxBanner:
                maxBanner = count*n
        return maxBanner
    pass
