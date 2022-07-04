from collections import deque

t = int(input())
for _  in range(t):
    funcs = input()
    length = int(input())
    arr = input()[1:-1].split(',')
    queue = deque(arr)

    flag = 0
    err = 0 

    if length == 0:
        queue = []

    for func in funcs:
        if func == 'R':
            flag += 1
        elif func == 'D':
            if len(queue) == 0:
                print('error')
                err = 1
                break
            else:
                if flag % 2==0:
                    queue.popleft()
                else:
                    queue.pop()
    
    if err == 0:
        if flag % 2 == 0:
            print('['+','.join(queue)+']')
        else:
            queue.reverse()
            print('['+','.join(queue)+']')

