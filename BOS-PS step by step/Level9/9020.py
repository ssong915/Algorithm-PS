def prime(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True	
	
arr = []								

for i in range(2,10000):						
    if prime(i):							
        arr.append(i)	

T = int(input())

for _ in range(T):
    num = int(input())
    half = num//2
    for i in range(half,1,-1):
        if i in arr:
            if num - i in arr:
                print(i,num-i)
                break
    
    