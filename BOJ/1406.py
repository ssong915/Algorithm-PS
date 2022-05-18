from sys import stdin

stack1 = list(stdin.readline().strip())
stack2 = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'P':
        stack1.append(command[1])

    elif command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    elif command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    else:
        stack1 = []

print(''.join(stack1+list(reversed(stack2))))
