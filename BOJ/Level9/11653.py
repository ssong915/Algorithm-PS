num = int(input())
div = 2

while True:
    if num % div == 0:
        print(div)
        num = num / div
    else:
        div += 1
    
    if num == 1:
        break