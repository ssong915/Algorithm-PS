S = input()
check = [-1]*26

for i in range(len(S)):
    if check[ord(S[i])-97] != -1: #처음 나온 수가 아니면
        continue
    else: #처음 나온 수라면 입력
        check[ord(S[i])-97] = i

for i in check:
    print(i,end=' ')
