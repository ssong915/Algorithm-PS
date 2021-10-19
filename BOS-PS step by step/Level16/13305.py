n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
del price[-1]

roadSum = sum(road)
priceMin = min(price)
priceLen = len(price)
result = 0

for i in range(priceLen-1):
    if (price[i] == priceMin):
        result += roadSum * price[i]
        break
    else:
        result += road[i]*price[i]
        roadSum -= road[i]

print(result)