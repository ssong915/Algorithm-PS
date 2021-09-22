num = int(input())
ans = num

for i in range(num):
    string = input()
    alp = []
    for j in range(len(string)-1):
        if string[j] != string[j+1]:
            if string[j] in string[j+1:]:
                ans -= 1
                break
        else:
            pass
        

print(ans)