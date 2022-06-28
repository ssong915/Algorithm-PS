num = int(input())

def hansu(num):
    ans = 0
    for i in range(1,num+1):
        if i <= 99 :
            ans = ans + 1
        else :
            nums = list(map(int, str(i)))
            if nums[0]-nums[1] == nums[1]-nums[2]:
                ans = ans + 1

    return ans

print(hansu(num))
        