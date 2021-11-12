n = int(input())

people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))

answer = [1] * n
for i in range(n):
    w, h = people[i][0],people[i][1]
    for j in range(n):
        if w < people[j][0] and h < people[j][1]:
            answer[i] += 1

for i in answer:
    print(i,end=' ')