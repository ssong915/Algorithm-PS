num = int(input())

for i in range(num):
    repete,text = input().split()
    repete = int(repete)
    for j in text:
        print(j * repete, end='')
    print()