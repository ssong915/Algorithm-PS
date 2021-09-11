while (1):
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: #에러뜨면 끝냄
        break