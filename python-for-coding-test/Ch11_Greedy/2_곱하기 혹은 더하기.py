data = input()
num_list = list((data))
num_list = list(map(int, num_list))

i = 0
result = 0

for num in num_list:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)