N = int(input())
ans_nums = set(map(int, input().split()))
M = int(input())
nums = list(map(int,input().split()))
for num in nums:
    if num in ans_nums:
        print(1)
    else:
        print(0)