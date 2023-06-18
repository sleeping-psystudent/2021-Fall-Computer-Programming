def solution(N, K):
    all_in = 0
    bet = 0
    
    while K > 0 and N > 0:
        if N%2 == 1:
            N = N-1
            bet += 1
            #print(N,bet,'bet')
        else:
            N = N/2
            all_in += 1
            #print(N,all_in,'all_in')
            K -= 1
                
    return int(N+bet+all_in-1)
          
    pass
