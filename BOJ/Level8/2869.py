# A, B, V = map(int, input().split())
# start = 0
# day = 1
# while True:
#     start += A
#     start -= B    
#     if V <= start :
#         print(day)
#         break

#     day += 1


a,b,v = map(int,input().split())
k = (v-b)/(a-b)
if k==int(k):
    print(int(k))
else:
    print(int(k)+1)