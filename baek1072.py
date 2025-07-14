a, b = input("판수, 승수:").split()

x = int(a)
y = int(b)
z = int((y/x) * 100)

if (z>=99):
    print(-1)
else:
    min = 0
    max = 1000000000    
    while min < max:
        mid = (min + max) // 2
        new = int(((y + mid) / (x + mid)) * 100)
        if new > z:
            max = mid -1
        else:
            min = mid +2
        
print(min)
        
        


    
#기존 승률에 몇번을 더해야 승률이 변하는지?
#형택이는 이제 절대지지 않는다 판수가 올라가면 승수도 같이올라감.
#만일 z가 절대 변하지 않는다? >> 판수=승수 일시 -1 출력
#이진 탐색으로 판수, 승수 늘려가면서 좁힌다.
#결론 끝
