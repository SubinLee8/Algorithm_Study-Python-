num=int(input())
direction=list(input().split())
location_l=1
location_r=1

for i in direction:
    if i=='R':
        location_r+=1
    if i=='U':
        location_l-=1
    if i=='L':
        location_r-=1
    if i=='D':
        location_l+=1
    if location_l==0:
        location_l+=1
    if location_r==0:
        location_l+=1

print(location_l,location_r)
    