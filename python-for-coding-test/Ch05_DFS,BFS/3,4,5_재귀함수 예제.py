def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 재귀함수를 종료합니다.')

def factorial_iterative(num):
    result = 1

    for i in range (1,num+1):
        result *= i
    return result

def factorial_function(num):
    if num <= 1:
        return 1
    return num * factorial_function(num-1)

recursive_function(1)
print('냅다 팩토리얼' , factorial_iterative(5))
print('재귀 팩토리얼' , factorial_function(5))