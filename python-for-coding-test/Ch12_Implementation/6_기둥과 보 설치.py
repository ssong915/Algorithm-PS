def possible (result):
    for x,y,a in result:
        if a == 0: # 기둥
            if y == 0 or (x-1,y,1) in result or (x,y-1,0) in result or (x,y,1) in result:
                # 바닥에 있거나 or 보의 한쪽 끝에 있거나 or 다른기둥위에있거나 or 보위에 있으면
                continue
            else:
                return False

        elif a == 1: # 보
            if ( (x-1,y,1) in result and (x+1,y,1) in result ) or ( (x,y-1,0) in result or (x+1,y-1,0) in result):
                # ( 양쪽 끝부분이 동시에 연결되어 있거나 ) or ( 보의 한쪽 끝부분이 기둥위에 있으면 ) 
                continue
            else:
                return False
    
    return True 

def solution(n, build_frame):
    result = set() 

    for (x,y,a,b) in build_frame:
        new = (x,y,a)
        if b == 1: # 설치
            result.add(new)
            if not possible(result): # 설치한게 불가능한 구조면
                result.remove(new) # 다시 삭제

        elif b==0 and new in result:
            result.remove(new) # 삭제
            if not possible(result): # 삭제한게 불가능한 구조면
                result.add(new) # 다시 설치

    answer = map(list,result)
    return sorted(answer)