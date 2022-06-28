import sys
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
for i in range(N):
    print(nums[i])