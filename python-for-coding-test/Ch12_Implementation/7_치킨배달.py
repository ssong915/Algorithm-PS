from itertools import combinations

n,m=map(int, input().split())
city= [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range (n):
    for j in range (n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

pick_chicken = list(combinations(chicken,m))

result=[0]*len(pick_chicken)

for j in range(len(pick_chicken)):
    for i in home:
        min_dis = 100
        for k in pick_chicken[j]:
            temp=abs(i[0]-k[0])+abs(i[1]-k[1])
            min_dis=min(min_dis,temp)
        result[j]+=min_dis

print(min(result))