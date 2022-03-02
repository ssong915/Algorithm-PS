num = int(input())
day = []
money = []
for _ in range(num):
    x,y = map(int,input().split())
    day.append(x)
    money.append(y)

dp = [0]*(num+1)
max_result = 0 
# 마지막 날 부터 뒤부터 확인
for i in reversed(range(num)):
    tmp = day[i] + i
    if tmp <= num:
        dp[i] = max(max_result,money[i]+dp[tmp])
        max_result = dp[i]
    else:
        dp[i]=max_result 
print(max_result)