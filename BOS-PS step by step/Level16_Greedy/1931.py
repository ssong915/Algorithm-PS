n = int(input())
conference = []
for i in range(n):
    start, end = map(int,input().split())
    conference.append([start,end])

conference = sorted(conference, key = lambda x:x[0])
conference = sorted(conference, key = lambda x:x[1])

temp = 0
result = 0
for i,j in conference:
    if i >= temp:
        temp = j
        result += 1

print(result)