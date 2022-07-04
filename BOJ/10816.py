n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
m_nums = list(map(int, input().split()))

ans = [0]*m

for i in range(m):
    num = ans[i]
    left = 0
    right = n-1
    mid = (left+right)//2
    if num > nums[mid]:
        left = mid+1
    elif num < nums[mid]:
        right = mid -1
    elif num == nums[mid]:
        ans[i]

for i in ans:
    print(i, end=' ')

