import math

N = int(input())

count = 0                                    
result = []

for _ in range(N):
    a, b = map(int, input().split())
    distance = b - a                        

    num = math.floor(math.sqrt(distance))    
    squared = num**2                

    if distance == squared:
        count = (num*2)-1

    elif squared < distance <= squared + num:
        count = (num*2)

    elif (squared + num) < distance:
        count = (num*2) + 1

    elif distance < 4:
        count = distance
    result.append(count)

for x in result:
    print(x)