input_string = input().upper() #MISSISSIPI
kindof_string = list(set(input_string)) #MISP
count_string = []

for string in kindof_string:
    count_string.append(input_string.count(string)) 
    # count 함수!
    # input_string.count(string) : input_string 에 있는 string 를 count 해줌
    # ex) MISSISSIPI 에 있는 M 의 수

# count_string = [1 4 4 1]

if count_string.count(max(count_string)) > 1:
    print("?")
    # [1 4 4 1] 중 max 4 갯수 count
    
else:
    print(kindof_string[count_string.index(max(count_string))])
    # index 함수!
    # count_string.index(max(count_string)) : "count_sting 의 최대"값을 가진 count_string의 index
