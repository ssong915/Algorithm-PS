arr = [10, 20, 10, 30, 20, 50]
n = len(arr)
dp = [1] * n
 
for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j]+ 1)
 
print(dp)
print(max(dp))