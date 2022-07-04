N = int(input())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

for num in arr:
    print(num,end = ' ')
