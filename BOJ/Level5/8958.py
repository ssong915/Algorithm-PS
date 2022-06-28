num = int(input())

for i in range(num): 
    arr = list(input())
    score = 0
    plus = 1
    for j in arr:
        if j =='O':
            score = score + plus
            plus = plus +1
        elif j == 'X':
            plus = 1
    print(score)