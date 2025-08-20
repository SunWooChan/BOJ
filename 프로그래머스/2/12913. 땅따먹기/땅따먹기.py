def solution(land):
    n = len(land)
    dp = [[0] * 4 for i in range(n)]
    
    dp[0] = land[0]
    
    for i in range(1, n):
        for j in range(4):
            for k in range(4):
                if k != j:
                    dp[i][j] = max(dp[i][j], dp[i-1][k] + land[i][j])
    answer = max(dp[n-1])
    return answer