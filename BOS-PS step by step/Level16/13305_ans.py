n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

priceMin = price[0]
priceLen = len(price)
result = 0

for i in range(priceLen-1):
    if (price[i] < priceMin):
        priceMin = price[i]
    result += priceMin * road[i]

print(result)