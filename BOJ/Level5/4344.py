num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]
    upper_avg = 0
    for i in arr[1:]:
        if i > avg:
            upper_avg += 1
    ans = (upper_avg/arr[0])*100
    print("{:.3f}%".format(ans))
