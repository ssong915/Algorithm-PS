hour,min = map(int, input().split())

if min >= 45: # 등호 성립도 생각했어야함~
    print(hour,min-45)
elif hour >0 and min < 45:
    print(hour-1,min+15)
else:
    print(23,min+15)