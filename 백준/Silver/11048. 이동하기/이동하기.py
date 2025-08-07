n, m = map(int, input().split())
# DP table과 일치하게 받기
arr = [[0] + list(map(int, input().split())) for _ in range(n)]
arr = [[0] * (m+1)] + arr

# DP table initialization
dp=[[0] * (m+1) for _ in range(n+1)]

# initialize value
dp[1][1] = arr[1][1]

for j in range(2, m+1):
	dp[1][j] = arr[1][j] + dp[1][j-1]

for i in range(2, n+1):
	dp[i][1] = arr[i][1] + dp[i-1][1]

# Bottom up
for i in range(2,n+1):
	for j in range(2,m+1):
		dp[i][j] = arr[i][j]
		dp[i][j] += max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

print(dp[n][m])
