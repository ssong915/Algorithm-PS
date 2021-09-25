num = int(input())

start = 1 
end = 1

mul = 1

while True :
    if start<= num <= end:
        print(mul)
        break
    else:
        start += 6*(mul-1)
        end += 6*mul
        mul += 1
        