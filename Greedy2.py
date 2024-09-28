num=int(input())
Horror=list(map(int,input().split()))

Horror.sort()


count=0 #현재 그룹 내 인원수
result=0 #그룹 수
j=Horror[0]

for i in Horror:
    count+=1 
    if count>=j:
        result+=1
        count=0
        j=i

print(result)









