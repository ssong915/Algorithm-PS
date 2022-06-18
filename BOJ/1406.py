import sys
stack1 = list(sys.stdin.readline().strip())
stack2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'P':
        stack1.append(command[1])

    elif command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    else:
        if stack1:
            stack1.pop()

print(''.join(stack1+list(reversed(stack2))))
