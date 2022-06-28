num1 = int(input())
choice = num1
num2 = 0
temp = 0
count = 0
while True:
    temp = num1//10 + num1%10
    num2 = (num1%10)*10 + temp%10
    count += 1
    num1 = num2
    if num2 == choice:
        break
print(count)