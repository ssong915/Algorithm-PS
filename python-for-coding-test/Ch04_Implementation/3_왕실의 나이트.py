n = input()
x = ord(n[0])-96
y = int(n[1])

steps = [(2,1),(2,-1),(-2,1),(-2,-2),(1,2),(1,-2),(-1,2),(-1,-2)]
result = 0

for step in steps:
    dx = x + step[0]
    dy = y + step[1]
    if ( dx<1 or dy<1 or dx>8 or dy>8):
        continue
    result += 1

print(result)

