n = int(input())
arr = list(map(int, input().split()))

arr.sort()
i = 0 
group = 0

while True:
    num = arr[i]
    i = i + num
    if i >= len(arr):
        break
    group += 1

print(group)