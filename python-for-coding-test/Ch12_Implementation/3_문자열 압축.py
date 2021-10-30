def solution(s):
    answer = len(s)
    for i in range(1, int(len(s)/2) +1): # i개씩 압축
        pos = 0 # 몇번째 처리 중?
        length = len(s) # 여기서 빼면서 계산

        while pos + i <= len(s): # 문자 끝까지 비교
            unit = s[pos:pos+i] # pos~ pos+i-1 까지
            pos += i
            cnt = 0 # 몇번 반복되나

            while pos + i <= len(s):
                unit2 = s[pos:pos+i]
                if(unit == unit2):
                    cnt += 1
                    pos += 1
                else:
                    break
            
            if cnt > 0: # 반복이 있으면
                length -= cnt * i
                if cnt < 9 :
                    length += 1
                elif cnt < 99:
                    length += 2
                elif cnt < 999:
                    length += 3
                else :
                    length += 4
            
        answer = min(answer,length)


    return answer
