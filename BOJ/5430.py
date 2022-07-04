from collections import deque
from sys import stdin, stdout

t = int(stdin.readline())
for _  in range(t):
    funcs = stdin.readline()
    length = stdin.readline().rstrip()
    arr = stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(arr)

    flag = 0
    err = 0 

    for func in funcs:
        if len(queue) == 0 or length == 0:
            print('error\n')
            err = 1
            break

        if func == 'R':
            flag += 1
        elif func == 'D':
            if flag % 2==0:
                queue.popleft()
            else:
                queue.pop()
    
    if err == 0:
        if flag % 2 == 0:
            print('['+','.join(queue)+']\n')
        else:
            queue.reverse()
            print('['+','.join(queue)+']\n')

