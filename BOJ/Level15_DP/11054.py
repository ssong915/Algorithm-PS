n = int(input())
a = list(map(int, input().split()))

inc_dp = [1]*n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            inc_dp[i] = max(inc_dp[j]+1, inc_dp[i])

dec_dp = [1]*n
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if a[i] > a[j]:
            dec_dp[i] = max(dec_dp[j]+1, dec_dp[i])

dp = [0]*n
for i in range(n):
    dp[i] = inc_dp[i]+dec_dp[i]-1

print(max(dp))
