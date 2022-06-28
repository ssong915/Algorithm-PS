# combinations 이용
from itertools import combinations

n,m = map(int,input().split())
arr = list(map(int, input().split()))

cases = list(combinations(arr,3))
max_sum = 0

for case in cases:
    temp = sum(case)
    if max_sum < temp <= m:
        max_sum = temp

print(max_sum)