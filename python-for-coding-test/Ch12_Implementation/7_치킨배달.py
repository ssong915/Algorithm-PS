from itertools import combinations

n,m=map(int, input().split())
city= [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range (n):
    for j in range (n):
        if city[i][j] == 1:
            home.append((i,j)) # home 에 집좌표 추가
        elif city[i][j] == 2:
            chicken.append((i,j)) # chicken 에 치킨집좌표 추가

pick_chicken = list(combinations(chicken,m)) # 치킨집을 m개 씩 조합하여 list화

result=[0]*len(pick_chicken) # 조합 수 만큼의 도시치킨거리 넣어줄 배열

for j in range(len(pick_chicken)):
    for i in home:
        min_dis = 100
        for k in pick_chicken[j]: # j 번째 조합 loop
            temp=abs(i[0]-k[0])+abs(i[1]-k[1]) # 치킨거리
            min_dis=min(min_dis,temp) # j 번째 조합 중 최소 치킨거리를 찾기위해
        result[j]+=min_dis # j 번째 도시치킨거리 += 치킨거리

print(min(result)) 