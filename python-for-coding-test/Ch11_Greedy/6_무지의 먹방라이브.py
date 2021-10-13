import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    pq = [] # 우선순위 큐 : 
    # 리스트를 사용하면 되기 때문에, heapq 사용시에 리스트를 계속 인자로 넘겨주어야함

    for i in range(len(food_times)):
        heapq.heappush(pq, (food_times[i], i + 1)) # heappush: 원소추가
    
    previous = 0
    now = 0
    length = len(food_times)

    while k - ((pq[0][0] - previous) * length) >= 0:
        now = heapq.heappop(pq)[0] # heappop: 원소삭제
        k -= ((now - previous) * length)
        length -= 1
        previous = now
    
    result = sorted(pq, key = lambda x:x[1])
    next = k % length

    return result[next][1]
    