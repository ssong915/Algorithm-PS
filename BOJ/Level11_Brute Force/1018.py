n , m = map(int,input().split())
board = []
for i in range(n):
    board.append(input())

answer = [] 
for i in range(n-7): # n행
    for j in range(m-7): # m열
        start_B = 0 # B로 시작하는 체스판 만들기
        start_W = 0 # W로 시작하는 체스판 만들기
        for a in range(i,i+8): # 8X8 로 나누기
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] == 'B': start_W+=1 
                    if board[a][b] == 'W': start_B+=1
                else:
                    if board[a][b] == 'B': start_B+=1
                    if board[a][b] == 'W': start_W+=1
                
        answer.append(min(start_W,start_B))

print(min(answer))
