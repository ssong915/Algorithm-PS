def solution(food_times, k):

    foods = len(food_times)
    if sum(food_times) <= k:
        return -1

    for i in range(foods):
        while k != 0:
            if food_times[i] != 0:
                food_times[i] -= food_times[i] -1

            k -= 1
            break
            
        answer = i+1
        print(answer)
        return answer


food_times = list(map(int, input().split()))
k = int(input())
ans = solution(food_times,k)