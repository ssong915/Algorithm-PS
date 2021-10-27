strings = input()
alp = []
sum = 0
for string in strings:
    if string.isalpha():
        alp.append(string)
    else:
        sum += int(string)

alp.sort()

alp.append(str(sum))

# 리스트를 문자열로 반환하여 출력!
print(''.join(alp))