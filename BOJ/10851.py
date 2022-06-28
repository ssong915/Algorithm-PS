N = int(input())
arr1 = list(map(int,input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
ans = []

arr1.sort()

for i in arr2:
    left = 0 
    right = N-1
    ans_exist = False

    while left <= right:
        mid = (left+right)//2

        if arr1[mid] < i:
            left = mid + 1
        elif arr1[mid] > i:
            right = mid -1
        else:
            ans_exist = True
            ans.append(1)
            break
    if not ans_exist :
        ans.append(0)

print(*ans)
