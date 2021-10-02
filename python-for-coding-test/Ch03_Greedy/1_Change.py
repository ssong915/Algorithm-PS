N = int(input())
ans = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    ans = ans + N//coin
    N = N % coin

print(ans)