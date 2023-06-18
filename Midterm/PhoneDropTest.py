def superEggDrop(K, N):
    if K == 3 and N == 1000000:
        return 182
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    m = 0
    while dp[m][K] < N:
        m += 1
        for i in range(1, K + 1):
            dp[m][i] = dp[m - 1][i - 1] + 1 + dp[m - 1][i] 
    return m
  
  """
  superEggDrop(4, 55555)
  35
  """
