n = int(input())

answer = 0 

for i in range(1,n+1): 
    temp = list(map(int,str(i))) # 198 ->[1,9,8]
    sum_num = i + sum(temp) # 198 + (1+9+8)
    if(sum_num==n):
        answer = i
        break

print(answer)

