N = int(input())
alp = []

for _ in range(N):
    alp.append(input())

alp = set(alp)  # 중복제거
alp = list(alp)
alp.sort()  # 정렬
alp.sort(key=len)

for a in alp:
    print(a)
