num = int(input())
dp = [[0]*num]*num
for i in range(num):
    dp[i] = list(map(int, input().split()))

for x in range(1, num):
    for y in range(x+1):
        if x == y:
            dp[x][y] = dp[x-1][y-1]+dp[x][y]
        elif y == 0:
            dp[x][y] = dp[x-1][y]+dp[x][y]
        else:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-1])+dp[x][y]

result = 0
for i in range(num):
    result = max(result, dp[num-1][i])
print(result)
