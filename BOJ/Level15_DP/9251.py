str1 = ' '+input()
str2 = ' '+input()
len_str1 =len(str1)
len_str2 =len(str2)
dp = [[0]*len_str2 for _ in range(len_str1)]

for i in range(1,len_str1):
    for j in range(1,len_str2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])