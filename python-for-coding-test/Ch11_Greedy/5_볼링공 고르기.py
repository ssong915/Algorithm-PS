n,m =  map(int, input().split())
arr = list(map(int, input().split()))
result = 0

length = len(arr)

for num in arr:
    result += (length - arr.count(num))

print(int(result/2))