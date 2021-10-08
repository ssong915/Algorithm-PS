num_list = input()
# num_list = list((data))
# num_list = list(map(int, num_list))

zero_ans = 0 
one_ans = 0
i = 0 

if num_list[0] == 0:
    zero_ans += 1
else:
    one_ans += 1

for i in range(len(num_list)-1):
    if num_list[i] != num_list[i+1]:
        if num_list[i+1]==1:
            one_ans+=1
        else:
            zero_ans+=1

print(min(zero_ans,one_ans))
