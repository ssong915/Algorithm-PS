def rotate(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def attach(i,j,key_len,new_lock,key):
    for x in range(key_len):
        for y in range(key_len):
            new_lock[x+i][y+j]+=key[x][y]

def check(new_lock,lock_len):
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len,lock_len*2):
            if new_lock[i][j]!=1 :
                return False
    return True

def detach(i,j,key_len,new_lock,key):
    for x in range(key_len):
        for y in range(key_len):
            new_lock[x+i][y+j]-=key[x][y]



def solution(key, lock):
    key_len = len(key)
    lock_len = len(lock)

    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

    for i in range(lock_len):
        for j in range(lock_len):
            new_lock[i + lock_len][j + lock_len] = lock[i][j]
            
    
    for _ in range(4):
        key = rotate(key)
        for i in range(1, lock_len*2):
            for j in range(1, lock_len*2):
                attach(i,j,key_len,new_lock,key)
                if check(new_lock,lock_len):
                    return True
                else:
                    detach(i,j,key_len,new_lock,key)
    
    return False

