n = int(input())
sul = [0]*10000
for i in range(n):
    sul[i] = int(input())

dp = [0] * n
dp[0] = sul[0]
if n > 1:
    dp[1] = sul[0]+sul[1]
if n > 2:
    dp[2] = max(sul[2]+dp[0], dp[1], sul[1]+sul[2])
if n > 3:
    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2]+sul[i], dp[i-3]+sul[i-1]+sul[i])

print(max(dp))
