String="02986"
result=int(String[0])

for i in range(1,len(String)):
    num=int(String[i])
    if num<=1 or result<=1:
        result+=num

    else:
        result*=num
    


print(result)
    
