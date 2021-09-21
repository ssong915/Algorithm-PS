remove = [] #생성자 있는 수들

def create(num):
    sum = num
    nums = list(map(int,str(num)))
    for i in nums:
        sum = sum + i
    return sum

for i in range(1,10001):
    creater = create(i)
    remove.append(creater)

for i in range(1,10001):
    if i in remove:
        pass
    else:
        print(i)
