num = int(input())

start = 1 
end = 1
plus = 1

upper = 0
lower = 0

while True :
    if start<= num <= end:
        if plus % 2 ==0 :
            upper = num - start + 1
            lower = ( plus + 1 ) - upper
        else:
            lower = num - start + 1
            upper = ( plus + 1 ) - lower       
        break
    else:
        start += plus
        plus += 1
        end += plus
          
print(f'{upper}/{lower}')