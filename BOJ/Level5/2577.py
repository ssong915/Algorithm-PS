A = int(input())
B = int(input())
C = int(input())

result = list(str(A*B*C))

for i in range(10):
    print(result.count(str(i))) 
    # result 안에 있는 i 를 count 해라