N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp=[[0]*(3) for _ in range(N)]

dp[0] = arr[0]
for n in range(1, N):
    dp[n][0] = min(dp[n-1][1], dp[n-1][2]) + arr[n][0]
    dp[n][1] = min(dp[n-1][0], dp[n-1][2]) + arr[n][1]
    dp[n][2] = min(dp[n-1][0], dp[n-1][1]) + arr[n][2]

print(min(dp[N-1]))